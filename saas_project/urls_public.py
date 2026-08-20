# saas_project/urls_public.py
from django.contrib import admin
from django.urls import path
from customers.views import public_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', public_home, name='public_home'),
]