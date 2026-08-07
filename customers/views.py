from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def public_home(request):  #public landing page:
    html = """
    <html>
        <body style="font-family: sans-serif; padding: 40px; text-align: center; background-color: #f8f9fa;">
            <h1 style="color: #0b57d0;">Your Awesome SaaS Platform</h1>
            <p>This is the public landing page served from the <strong>public</strong> schema.</p>
            <p>Imagine your pricing tables and a "Register your Company" button here.</p>
        </body>
    </html>
    """
    return HttpResponse(html)