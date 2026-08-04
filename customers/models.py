from django.db import models
from django_tenants.models import DomainMixin
from tenant_users.tenants.models import TenantBase, UserProfile

# Create your models here.
class Client(TenantBase):
    name = models.CharField(max_length=100)
    paid_until = models.DateField(null=True, blank=True)
    on_trial = models.BooleanField(default=True)
    auto_create_schema = True

class Domain(DomainMixin):
    pass

class TenantUser(UserProfile):
    name = models.CharField(max_length=100, blank=True)
    # We don't need to define email or password here, 
    # UserProfile handles that automatically!