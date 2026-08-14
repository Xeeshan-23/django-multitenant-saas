from django.shortcuts import render, redirect
from .models import Project # Ensure you import the Project model here

def home(request):
    # handle the form submission for creating a new project:
    if request.method == 'POST':
        name = request.POST.get('name')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')

        # create the project in the current tenant's schema:
        Project.objects.create(
            name=name,
            status=status,
            due_date=due_date
        )
        # Redirect back to the dashboard to prevent double-submissions on refresh
        return redirect('tenant_home')
    # Fetch all projects for the GET request
    projects = Project.objects.all() 
    
    context = {
        'tenant': request.tenant,
        'projects': projects, # This is the crucial line linking the database to your HTML template
    }
    return render(request, 'core/dashboard.html', context)