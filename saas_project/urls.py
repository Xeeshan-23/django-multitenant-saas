# saas_project/urls.py
from django.urls import path
from core.views import home, update_project, clear_notifications

urlpatterns = [
    path('', home, name='tenant_home'),
    path('projects/', home, name='tenant_projects'), # Temporarily routing to home
    path('team/', home, name='tenant_team'),
    path('project/update/<int:project_id>/', update_project, name='update_project'),
    path('notifications/clear/', clear_notifications, name='clear_notifications'),
]