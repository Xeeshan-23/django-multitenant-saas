# Django Tenant Forge 
A scalable, production-ready B2B SaaS boilerplate built with Django and PostgreSQL.
This template provides a robust foundation for building multi-tenant applications using schema-based isolation, ensuring strict data separation between clients while maintaining a single, unified codebase. It includes dynamic subdomain routing and a global authentication system.

#  Architecture Overview
This project uses the Shared Database, Separate Schemas approach to multi-tenancy.

**1. Data Security:** Every tenant (customer) gets their own isolated PostgreSQL schema. A bug in the application code cannot accidentally leak data across tenants because the database itself enforces the boundaries.

**2. Cost Efficiency:** All tenants share the same database instance and application server, minimizing infrastructure overhead.

**3. Global Authentication:** Users are stored in the shared public schema. A user can log in once and access multiple tenant environments (based on their permissions) without needing separate accounts.

#  Key Features:

**PostgreSQL Schema Isolation:** Powered by django-tenants.

**Global User Management:** Centralized authentication powered by django-tenant-users.

**Dynamic Routing:** Automatically routes traffic to the correct schema based on the incoming subdomain (e.g., alpha.yourdomain.com).

**Clean App Structure:** Clear separation between SHARED_APPS (infrastructure/global data) and TENANT_APPS (tenant-specific business logic).
# Technology Stack

**Backend:** Python, Django 5.x

**Database:** PostgreSQL

**Multi-Tenancy:** django-tenants, django-tenant-users
# Getting Started
Follow these instructions to get the project running on your local machine.

**Prerequisites**

Python 3.10+

PostgreSQL running locally (or via Docker)

# 1. Clone & Install

git clone https://github.com/Xeeshan-23/django-multitenant-saas.git

cd django-tenant-forge

**Create and activate a virtual environment**

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

**Install dependencies**

pip install -r requirements.txt

# 2. Database Configuration

1. Create a new PostgreSQL database (e.g., saas_project) using pgAdmin or the command line.

2. Update the DATABASES configuration in settings.py with your local PostgreSQL credentials (User, Password, Host, Port).

# 3. Apply Migrations

Run the specialized migration commands to build the shared architecture:

python manage.py makemigrations

python manage.py migrate_schemas --shared

# 4. Provision the Public Tenant

Initialize the primary public schema and create your global superuser account:

python manage.py create_public_tenant --domain_url localhost --owner_email admin@example.com

# 5. Create a Test Tenant

To test the multi-tenant routing, use the Django shell to spin up a local tenant environment:

python manage.py shell

from customers.models import Client, Domain

# Create the isolated tenant schema
tenant1 = Client(schema_name='tenant_alpha', name='Alpha Corp', paid_until='2027-12-31', on_trial=False)
tenant1.save()

# Map a local subdomain to the tenant
domain1 = Domain(domain='alpha.localhost', tenant=tenant1, is_primary=True)
domain1.save()
exit()

Note: You must add 127.0.0.1 alpha.localhost to your local hosts file to test this in your browser.

# 6. Run the Server

Start the development server:

python manage.py runserver 8080

 Visit http://localhost:8080 to see the public landing page.
 
 Visit http://alpha.localhost:8080 to see the isolated tenant environment.
