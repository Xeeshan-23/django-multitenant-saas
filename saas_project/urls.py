# saas_project/urls.py
from django.urls import path
from core.views import home # Importing the function you actually have

urlpatterns = [
    path('', home, name='tenant_home'),
]