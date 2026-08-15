from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Notification

def home(request):
    # Handle NEW Project Creation
    if request.method == 'POST':
        name = request.POST.get('name')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        
        Project.objects.create(name=name, status=status, due_date=due_date)
        
        # Trigger a Notification
        Notification.objects.create(message=f"New project '{name}' was created.")
        return redirect('tenant_home')

    # Fetch data for the dashboard
    projects = Project.objects.all() 
    notifications = Notification.objects.filter(is_read=False)[:5] # Get top 5 unread
    
    context = {
        'tenant': request.tenant,
        'projects': projects,
        'notifications': notifications,
    }
    return render(request, 'core/dashboard.html', context)

# View to handle updating existing projects
def update_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        project.name = request.POST.get('name')
        project.status = request.POST.get('status')
        project.due_date = request.POST.get('due_date')
        project.save()
        
        # Trigger a Notification
        Notification.objects.create(message=f"Project '{project.name}' was updated.")
        
    return redirect('tenant_home')

def clear_notifications(request):
    if request.method == 'POST':
        # Find all unread notifications in this tenant's schema and mark them as read
        Notification.objects.filter(is_read=False).update(is_read=True)
        
    return redirect('tenant_home')