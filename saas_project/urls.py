# saas_project/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from core.views import home, update_project, clear_notifications

urlpatterns = [
    path('', home, name='tenant_home'),
    path('projects/', home, name='tenant_projects'), # Temporarily routing to home
    path('team/', home, name='tenant_team'),
    path('project/update/<int:project_id>/', update_project, name='update_project'),
    path('notifications/clear/', clear_notifications, name='clear_notifications'),
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]