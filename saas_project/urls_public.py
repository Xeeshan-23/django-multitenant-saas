# saas_project/urls_public.py
from django.contrib import admin
from django.urls import path
from core.views import public_home # Importing from core now

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', public_home, name='public_home'),
]