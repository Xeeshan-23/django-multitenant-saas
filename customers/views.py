from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .models import Client, Domain
from datetime import date, timedelta


def public_home(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        subdomain = request.POST.get('subdomain').lower().replace(" ", "")
        email = request.POST.get('email')
        password = request.POST.get('password')

        User = get_user_model()

        user, created = User.objects.get_or_create(email=email)
        if created:
            user.set_password(password)
            user.save()

        schema_name = f"tenant_{subdomain}"
        
        trial_end = date.today() + timedelta(days=30) 
        
        tenant = Client(
            schema_name=schema_name,
            name=company_name,
            paid_until=trial_end,
            on_trial=True,
            owner=user
        )
        tenant.save() 

        # Route the Subdomain
        domain_name = f"{subdomain}.localhost"
        domain = Domain(domain=domain_name, tenant=tenant, is_primary=True)
        domain.save()

        # grant this user Admin access to their new workspace
        tenant.add_user(user, is_superuser=True, is_staff=True)

        # redirect them to their brand new isolated login page
        return redirect(f"http://{domain_name}:8080/login/")

    return render(request, 'customers/public_home.html')