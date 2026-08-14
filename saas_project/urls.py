# saas_project/urls.py
from django.urls import path
from core.views import home 

urlpatterns = [
    path('', home, name='tenant_home'),
    path('projects/', home, name='tenant_projects'), # Temporarily routing to home
    path('team/', home, name='tenant_team'),
]