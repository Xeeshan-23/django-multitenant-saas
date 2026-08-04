from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db import connection

def home(request):
    # request.tenant is automatically injected by the TenantMainMiddleware!
    tenant_name = request.tenant.name 
    schema_name = connection.schema_name
    
    html = f"""
    <html>
        <body style="font-family: sans-serif; padding: 40px; text-align: center;">
            <h1>Welcome to {tenant_name}!</h1>
            <p>You are successfully querying the isolated PostgreSQL schema: <strong>{schema_name}</strong></p>
        </body>
    </html>
    """
    return HttpResponse(html)
