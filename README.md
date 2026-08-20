# Django Tenant Forge 🏢
A scalable, production-ready B2B SaaS boilerplate built with Django and PostgreSQL. 

This template provides a robust foundation for building multi-tenant applications using schema-based isolation, ensuring strict data separation between clients while maintaining a single, unified codebase. It includes automated tenant provisioning, dynamic subdomain routing, and a global authentication system.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/87659661-24da-405b-9895-bc04aa0d6e2b" />

## 🏗️ Architecture Overview
This project uses the **Shared Database, Separate Schemas** approach to multi-tenancy.

* **Data Security:** Every tenant (customer) gets their own isolated PostgreSQL schema. A bug in the application code cannot accidentally leak data across tenants because the database itself enforces the boundaries.
* **Cost Efficiency:** All tenants share the same database instance and application server, minimizing infrastructure overhead.
* **Global Authentication:** Users are stored in the shared public schema. A user can log in once and access multiple tenant environments (based on their permissions) without needing separate accounts.

## ✨ Key Features
* **Automated Provisioning Engine:** A public-facing onboarding flow that dynamically generates database schemas, registers admin accounts, and provisions custom subdomains instantly via a UI form.
* **Complete CRUD Lifecycle:** An interactive, isolated workspace dashboard with full Create, Read, Update, and Delete capabilities for project management.
* **Real-time Notification Engine:** An integrated alerting system that tracks workspace activity (e.g., project creations and deletions).
* **PostgreSQL Schema Isolation:** Powered by `django-tenants`.
* **Global User Management:** Centralized authentication powered by `django-tenant-users`.
* **Dynamic Routing:** Automatically routes traffic to the correct schema based on the incoming subdomain (e.g., `alpha.localhost`).
* **Clean App Structure:** Clear separation between `SHARED_APPS` (infrastructure/global data) and `TENANT_APPS` (tenant-specific business logic).

## 🛠️ Technology Stack
* **Backend:** Python, Django 5.x
* **Database:** PostgreSQL
* **Multi-Tenancy:** `django-tenants`, `django-tenant-users`
* **Frontend:** Tailwind CSS, HTML5, Vanilla JavaScript

## 🚀 Getting Started
Follow these instructions to get the project running on your local machine.

### Prerequisites
* Python 3.10+
* PostgreSQL running locally (or via Docker)

### 1. Clone & Install
```bash
git clone https://github.com/Xeeshan-23/django-multitenant-saas.git
cd django-multitenant-saas
```

**Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

# 2. Database Configuration

1. Create a new PostgreSQL database (e.g., saas_project) using pgAdmin or the command line.

2. Update the DATABASES configuration in settings.py with your local PostgreSQL credentials (User, Password, Host, Port).

# 3. Apply Migrations

Run the specialized migration commands to build the shared architecture:
```bash
python manage.py makemigrations
python manage.py migrate_schemas --shared
python manage.py migrate_schemas
```

# 4. Initialize the Public Tenant

To enable the public landing page and routing, open the Django shell (python manage.py shell) and execute:
```bash
from customers.models import Client, Domain
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()
admin_user, _ = User.objects.get_or_create(email='admin@tenantforge.com', defaults={'is_superuser': True, 'is_staff': True})

public_tenant, _ = Client.objects.get_or_create(
    schema_name='public',
    defaults={'name': 'TenantForge Public', 'paid_until': datetime.date(2030, 1, 1), 'on_trial': False, 'owner': admin_user}
)
Domain.objects.get_or_create(domain='localhost', defaults={'tenant': public_tenant, 'is_primary': True})
exit()
```

# 5. Run the Server & Test Automated Provisioning

Start the development server on port 8080 (required for local subdomain routing):
```bash
python manage.py runserver 8080
```
1. Visit http://localhost:8080 to see the public landing page.

2. Fill out the "Create Your Workspace" form to test the automated provisioning engine.

3. Upon submission, the system will instantly build an isolated schema and redirect you to your newly generated tenant subdomain (e.g., http://companyname.localhost:8080/login/).
