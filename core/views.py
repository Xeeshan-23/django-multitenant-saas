from django.shortcuts import render
from .models import Project # Ensure you import the Project model here

def home(request):
    # Fetch all projects (the middleware automatically filters this to the active tenant's schema!)
    projects = Project.objects.all() 
    
    context = {
        'tenant': request.tenant,
        'projects': projects, # This is the crucial line linking the database to your HTML template
    }
    return render(request, 'core/dashboard.html', context)