---
name: django
description: Complete Django development skill covering Django framework architecture, MVT pattern, models, ORM, views, templates, APIs, authentication, security, database integration, Django REST Framework, testing, deployment, scalability, and enterprise Django application development.
---

# Django Skill

# Skill Instructions

You are an expert Django backend engineer.

Your responsibility is to design, develop, review, debug, optimize, secure, and maintain production-ready Django applications.

You must think like:

- Senior Django Developer
- Python Backend Engineer
- Backend Architect
- API Developer
- Database Engineer
- Security Engineer
- Cloud Engineer
- Code Reviewer

Always generate:

- Clean Django architecture
- Maintainable applications
- Secure implementations
- Scalable backend systems
- Production-ready code
- Industry-standard solutions

---

# Django Overview

Django is a high-level Python web framework used for building:

- Enterprise web applications
- REST APIs
- Content management systems
- E-commerce platforms
- SaaS applications
- Admin dashboards
- Large-scale backend systems

---

# Django Philosophy

Follow Django principles:

- Don't Repeat Yourself (DRY)
- Explicit is better than implicit
- Security by default
- Rapid development
- Clean architecture

---

# Django Core Concepts

Master:

- Projects
- Applications
- Models
- Views
- Templates
- URLs
- Middleware
- ORM
- Admin panel
- Forms
- Authentication
- Security

---

# Django Architecture

Django follows MVT architecture.

```
Client Request

      |

URL Dispatcher

      |

View

      |

Model

      |

Database

      |

Template

      |

Response
```

---

# MVT Pattern

## Model

Responsible for:

- Database structure
- Data management
- Business entities

---

## View

Responsible for:

- Request handling
- Business logic
- Response generation

---

## Template

Responsible for:

- User interface
- HTML rendering
- Presentation layer

---

# Django Installation

Install Django:

```bash
pip install django
```

Check version:

```bash
django-admin --version
```

---

# Creating Django Project

Create project:

```bash
django-admin startproject projectname
```

Project structure:

```
projectname

├── manage.py

└── projectname

    ├── settings.py

    ├── urls.py

    ├── asgi.py

    └── wsgi.py
```

---

# Django Application

Django applications represent modules.

Examples:

```
users

products

orders

payments

reports
```

---

# Creating Django App

Command:

```bash
python manage.py startapp users
```

App structure:

```
users

├── models.py

├── views.py

├── urls.py

├── admin.py

├── apps.py

└── tests.py
```

---

# Django Settings

Master configuration management.

Important settings:

- INSTALLED_APPS
- DATABASES
- MIDDLEWARE
- STATIC_FILES
- MEDIA_FILES
- SECRET_KEY
- ALLOWED_HOSTS

---

# Django Project Structure

Enterprise structure:

```
project

├── apps

│
├── config

│
├── common

│
├── api

│
├── services

│
├── repositories

│
├── middleware

│
├── utils

│
├── tests

│
└── manage.py
```

---

# Django URL Routing

Master URL configuration.

Flow:

```
Request

 |

urls.py

 |

View Function

 |

Response
```

---

# URL Patterns

Example:

```python
from django.urls import path

urlpatterns = [

path(
"users/",
users_view
)

]
```

---

# URL Names

Always use named URLs.

Example:

```python
path(
"login/",
login_view,
name="login"
)
```

Benefits:

- Easy maintenance
- URL changes without breaking code

---

# Django Views

Views handle application logic.

Types:

- Function Based Views
- Class Based Views

---

# Function Based Views

Example:

```python
def home(request):

    return HttpResponse(
    "Hello"
    )
```

---

# Class Based Views

Advantages:

- Reusable
- Extensible
- Object-oriented

Example:

```python
class UserView(View):

    def get(self,request):

        pass
```

---

# Generic Class Based Views

Master:

- ListView
- DetailView
- CreateView
- UpdateView
- DeleteView

---

# Django Models

Models define database tables.

Example:

```python
class User(models.Model):

    name =
    models.CharField(
    max_length=100
    )

```

---

# Django Model Fields

Master:

## Text Fields

- CharField
- TextField

---

## Number Fields

- IntegerField
- DecimalField
- FloatField

---

## Date Fields

- DateField
- DateTimeField

---

## Boolean Fields

- BooleanField

---

## File Fields

- FileField
- ImageField

---

# Model Relationships

Master:

- One-to-One
- One-to-Many
- Many-to-Many

---

# One To One Relationship

Example:

```
User

|

Profile
```

Use:

```python
OneToOneField()
```

---

# One To Many Relationship

Example:

```
Customer

 |

Orders
```

Use:

```python
ForeignKey()
```

---

# Many To Many Relationship

Example:

```
Student

 |

Courses
```

Use:

```python
ManyToManyField()
```

---

# Django ORM

Master Django Object Relational Mapper.

ORM allows:

- Database queries using Python
- Query optimization
- Database abstraction

---

# Django QuerySet

Master:

- Filtering
- Ordering
- Aggregation
- Annotation
- Joins

---

# Query Examples

Get all:

```python
User.objects.all()
```

Filter:

```python
User.objects.filter(
active=True
)
```

Get:

```python
User.objects.get(
id=1
)
```

---

# Django Migrations

Manage database schema changes.

Commands:

Create migration:

```bash
python manage.py makemigrations
```

Apply:

```bash
python manage.py migrate
```

---

# Migration Best Practices

Follow:

- Small migrations
- Review generated SQL
- Backup database
- Test migrations

---

# Django Admin Panel

Django provides built-in admin.

Features:

- CRUD operations
- User management
- Data management
- Internal dashboards

---

# Register Model

Example:

```python
admin.site.register(
User
)
```

---

# Customize Admin

Customize:

- List display
- Filters
- Search
- Actions
- Permissions

---

# Django Forms

Forms handle:

- User input
- Validation
- Data processing

---

# Form Types

Master:

- Django Forms
- Model Forms

---

# Model Forms

Automatically generate forms from models.

Example:

```python
class UserForm(
forms.ModelForm
):

    class Meta:

        model=User
```

---

# Django Templates

Template engine for HTML rendering.

Understand:

- Variables
- Tags
- Filters
- Template inheritance

---

# Template Inheritance

Create reusable layouts.

Example:

```
base.html

 |

child templates
```

---

# Static Files

Manage:

- CSS
- JavaScript
- Images

Configuration:

```python
STATIC_URL
```

---

# Media Files

Handle uploaded files.

Configuration:

```python
MEDIA_URL

MEDIA_ROOT
```

---

# Django Middleware

Middleware processes requests globally.

Uses:

- Authentication
- Logging
- Security
- Request modification

---

# Custom Middleware

Create middleware for:

- Request tracking
- User activity
- Security checks
- Performance monitoring

---

````markdown id="djangopart2"
# Django REST Framework (DRF)

Master Django REST Framework for building production-ready APIs.

Django REST Framework provides:

- REST API development
- Serialization
- Authentication
- Permissions
- API documentation
- Browsable API
- Viewsets
- Routers

---

# DRF Installation

Install:

```bash
pip install djangorestframework
```

Add:

```python
INSTALLED_APPS = [

'rest_framework'

]
```

---

# DRF Architecture

Follow:

```
Client

 |

API Endpoint

 |

View / ViewSet

 |

Serializer

 |

Model

 |

Database
```

---

# REST API Concepts

Master:

- Resources
- HTTP methods
- Status codes
- API contracts
- Versioning
- Pagination
- Filtering

---

# HTTP Methods

GET:

Retrieve data

POST:

Create data

PUT:

Replace complete data

PATCH:

Update partial data

DELETE:

Remove data

---

# DRF Serializers

Serializers convert:

```
Python Objects

        |

JSON

        |

Client Response
```

---

# Serializer Types

Master:

- Serializer
- ModelSerializer

---

# ModelSerializer

Automatically creates fields from models.

Example:

```python
class UserSerializer(
serializers.ModelSerializer
):

    class Meta:

        model = User

        fields = "__all__"
```

---

# Serializer Validation

Validate:

- Required fields
- Data types
- Business rules
- Custom conditions

---

# Custom Serializer Validation

Example:

```python
def validate_email(
self,
value
):

    return value
```

---

# DRF Views

Master:

- APIView
- Generic Views
- ViewSets

---

# APIView

Provides:

- Full control
- Custom API logic
- Manual request handling

Example:

```python
class UserAPI(
APIView
):

    def get(
    self,
    request
    ):

        pass
```

---

# Generic API Views

Master:

- ListAPIView
- CreateAPIView
- RetrieveAPIView
- UpdateAPIView
- DestroyAPIView

---

# ViewSets

ViewSets combine related operations.

Example:

```python
class UserViewSet(
ModelViewSet
):

    queryset = User.objects.all()

    serializer_class =
    UserSerializer
```

---

# DRF Routers

Routers automatically create URLs.

Example:

```python
router.register(
"users",
UserViewSet
)
```

Generated:

```
GET /users

POST /users

GET /users/id

PUT /users/id

DELETE /users/id
```

---

# API Response Handling

Use:

```python
Response()
```

Example:

```python
return Response(
{
"success":True
}
)
```

---

# HTTP Status Codes

Master:

## Success

```
200 OK

201 Created

204 No Content
```

---

## Client Errors

```
400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found
```

---

## Server Errors

```
500 Internal Server Error
```

---

# API Pagination

Handle large datasets.

Types:

- Page pagination
- Limit offset pagination
- Cursor pagination

---

# DRF Filtering

Implement:

- Search
- Ordering
- Filtering

Library:

```bash
pip install django-filter
```

---

# API Versioning

Support multiple API versions.

Example:

```
/api/v1/users

/api/v2/users
```

Benefits:

- Backward compatibility
- Safe upgrades

---

# Authentication in Django

Master:

- Session authentication
- Token authentication
- JWT authentication
- OAuth

---

# Django Authentication System

Built-in features:

- Users
- Groups
- Permissions
- Password management
- Sessions

---

# Custom User Model

Best practice:

Create custom user model before production.

Example:

```python
class User(
AbstractUser
):

    pass
```

---

# JWT Authentication

Use:

```
djangorestframework-simplejwt
```

Install:

```bash
pip install djangorestframework-simplejwt
```

---

# JWT Flow

```
Login

 |

Username + Password

 |

Generate Access Token

 |

Generate Refresh Token

 |

API Request

 |

Validate Token

 |

Allow Access
```

---

# JWT Configuration

Configure:

- Access token expiry
- Refresh token expiry
- Token rotation
- Blacklisting

---

# Permissions in DRF

Control API access.

Types:

- AllowAny
- IsAuthenticated
- IsAdminUser
- Custom permissions

---

# Custom Permissions

Example:

```python
class IsOwner(
BasePermission
):

    pass
```

---

# Role Based Access Control

Implement:

```
User

 |

Role

 |

Permissions

 |

Resources
```

---

# Django Signals

Signals allow communication between components.

Common signals:

- pre_save
- post_save
- pre_delete
- post_delete

---

# Signal Use Cases

Use for:

- User profile creation
- Audit logging
- Notifications
- Data synchronization

---

# Signal Example

```python
@receiver(
post_save,
sender=User
)

def create_profile(
sender,
instance,
**kwargs
):

    pass
```

---

# Django Service Layer

For enterprise applications.

Avoid putting business logic inside:

- Views
- Models

Use:

```
View

 |

Service

 |

Repository

 |

Database
```

---

# Django Repository Pattern

Repository handles:

- Database queries
- Data access
- Persistence logic

Benefits:

- Better testing
- Cleaner architecture
- Database abstraction

---

# Django Managers

Custom managers provide reusable queries.

Example:

```python
class ActiveManager(
models.Manager
):

    pass
```

---

# Advanced Django ORM

Master:

- select_related()
- prefetch_related()
- annotate()
- aggregate()
- F expressions
- Q objects

---

# Query Optimization

Avoid:

## N+1 Query Problem

Bad:

```
Get Users

Loop Users

Get Profile Each Time
```

---

# Solution

Use:

```python
select_related()
```

and:

```python
prefetch_related()
```

---

# Database Transactions

Use:

```python
transaction.atomic()
```

Example:

```
Create Order

+

Update Inventory

+

Payment

```

All succeed or rollback.

---

# PostgreSQL with Django

Recommended production database.

Features:

- Advanced queries
- JSON fields
- Full-text search
- Performance

---

# Database Configuration

Example:

```python
DATABASES = {

'default': {

'ENGINE':
'django.db.backends.postgresql',

}

}
```

---

# Django Cache Framework

Improve performance using caching.

Cache types:

- Memory cache
- Redis cache
- Database cache

---

# Redis with Django

Use Redis for:

- API caching
- Sessions
- Background jobs
- Rate limiting

Install:

```bash
pip install redis
```

---

# Django Background Tasks

Handle asynchronous operations.

Use:

- Celery
- Django Q
- RQ

---

# Celery with Django

Use cases:

- Email sending
- Reports
- Image processing
- Long-running tasks

---

# Celery Architecture

```
Django Application

 |

Task Queue

 |

Worker

 |

Task Execution
```

---

# Message Brokers

Supported:

- Redis
- RabbitMQ

---

# Email Integration

Implement:

- SMTP
- SendGrid
- AWS SES

Use cases:

- Welcome emails
- Password reset
- Notifications

---

# File Uploads

Handle:

- Images
- Documents
- Videos

Django provides:

- FileField
- ImageField

---

# File Storage

Production storage:

- AWS S3
- Azure Blob Storage
- Google Cloud Storage

---

# Image Processing

Libraries:

- Pillow
- OpenCV

Operations:

- Resize
- Compress
- Convert

---

# Django Security

Master Django security features.

Django provides:

- CSRF protection
- SQL injection protection
- XSS protection
- Clickjacking protection
- Secure authentication

---

````markdown id="djangopart3"
# Django Security

Master secure Django application development.

Security must be implemented at:

- Application level
- API level
- Database level
- Authentication level
- Deployment level

---

# Django Security Principles

Follow:

- Secure by default
- Validate all inputs
- Protect sensitive data
- Apply least privilege
- Keep dependencies updated
- Monitor security events

---

# Django Built-in Security Features

Django provides:

- CSRF protection
- SQL injection prevention
- XSS protection
- Clickjacking protection
- Secure password hashing
- Session security

---

# Cross Site Request Forgery (CSRF)

CSRF attacks force users to perform unwanted actions.

Django protects using:

- CSRF tokens
- Middleware protection

---

# CSRF Token Usage

Template example:

```html
<form method="post">

{% csrf_token %}

<button>
Submit
</button>

</form>
```

---

# Cross Site Scripting (XSS)

Protect against malicious scripts.

Django provides:

- Automatic HTML escaping
- Safe template rendering

---

# SQL Injection Prevention

Django ORM protects against SQL injection.

Avoid:

```python
raw_sql(user_input)
```

Prefer:

```python
User.objects.filter(
name=username
)
```

---

# Clickjacking Protection

Prevent website embedding attacks.

Use:

```python
X_FRAME_OPTIONS = "DENY"
```

---

# Secure Cookies

Configure:

```python
SESSION_COOKIE_SECURE=True

CSRF_COOKIE_SECURE=True

SESSION_COOKIE_HTTPONLY=True
```

---

# HTTPS Security

Production Django applications should use:

- HTTPS
- SSL certificates
- Secure headers
- HSTS

---

# Security Headers

Configure:

```python
SECURE_HSTS_SECONDS
```

Protection:

- HTTPS enforcement
- Browser security rules

---

# Authentication Security

Implement:

- Strong passwords
- Account lockout
- MFA
- Secure sessions
- Token expiration

---

# Password Hashing

Django uses secure password hashing.

Supported:

- PBKDF2
- Argon2
- BCrypt

---

# Custom Authentication Backend

Create custom authentication logic.

Examples:

- Email login
- Social login
- Enterprise SSO

---

# OAuth Integration

Integrate:

- Google
- GitHub
- Microsoft
- Azure AD

Libraries:

- django-allauth
- OAuth Toolkit

---

# API Security

Secure Django APIs.

Implement:

- JWT authentication
- Permission classes
- Rate limiting
- Request validation

---

# API Rate Limiting

Protect against:

- Brute force
- API abuse
- DDoS attempts

Libraries:

- django-ratelimit
- DRF throttling

---

# Dependency Security

Monitor packages.

Tools:

- pip audit
- Safety
- Dependabot
- Snyk

---

# Django Testing

Master complete Django testing.

Testing types:

- Unit testing
- Integration testing
- API testing
- End-to-end testing

---

# Django Test Framework

Built-in:

```python
django.test
```

Provides:

- TestCase
- Client
- Fixtures
- Assertions

---

# Django TestCase

Example:

```python
from django.test import TestCase

class UserTest(
TestCase
):

    def test_user_creation(self):

        self.assertTrue(True)
```

---

# Testing Models

Test:

- Model creation
- Validation
- Relationships
- Custom methods

---

# Testing Views

Test:

- HTTP responses
- Authentication
- Permissions
- Redirects

---

# Testing APIs

Use:

- DRF APITestCase
- pytest-django

---

# API Test Example

```python
response =
self.client.get(
"/api/users/"
)

self.assertEqual(
response.status_code,
200
)
```

---

# PyTest with Django

Install:

```bash
pip install pytest pytest-django
```

---

# PyTest Benefits

Provides:

- Fixtures
- Better syntax
- Plugins
- Faster testing

---

# Mocking in Django

Mock:

- External APIs
- Email services
- Payment systems
- Cloud storage

Library:

```python
unittest.mock
```

---

# Test Coverage

Measure:

- Code coverage
- Branch coverage
- Function coverage

Tool:

```bash
coverage.py
```

---

# Django Logging

Implement structured logging.

Track:

- Requests
- Errors
- Security events
- Performance issues

---

# Django Logging Configuration

Configure:

```python
LOGGING = {

}

```

---

# Logging Levels

Understand:

```
DEBUG

INFO

WARNING

ERROR

CRITICAL
```

---

# Monitoring Django Applications

Monitor:

- CPU
- Memory
- Database queries
- API latency
- Errors

---

# Monitoring Tools

Use:

- Prometheus
- Grafana
- Datadog
- New Relic
- Sentry

---

# Error Tracking

Use:

- Sentry
- Rollbar

Track:

- Exceptions
- Stack traces
- User impact

---

# Django Performance Optimization

Optimize:

- Database queries
- Templates
- APIs
- Caching
- Background tasks

---

# Database Optimization

Improve using:

- Indexes
- Query optimization
- select_related()
- prefetch_related()

---

# Django Query Profiling

Tools:

- Django Debug Toolbar
- Silk

---

# Django Debug Toolbar

Provides:

- SQL queries
- Request timing
- Template rendering details

---

# Caching Strategies

Use:

## Full Page Cache

Cache complete pages.

---

## Fragment Cache

Cache template sections.

---

## API Cache

Cache API responses.

---

# Redis Cache Architecture

```
Request

 |

Django View

 |

Check Redis

 |

Cache Hit

 |

Return Response


Cache Miss

 |

Database

 |

Store Cache
```

---

# Django Async Support

Modern Django supports asynchronous programming.

Use:

- Async views
- Async ORM operations
- Async tasks

---

# Async View Example

```python
async def view(
request
):

    return JsonResponse({})
```

---

# Django Deployment

Deploy Django applications professionally.

Common stack:

```
Nginx

 |

Gunicorn

 |

Django

 |

PostgreSQL

 |

Redis
```

---

# Gunicorn

Production WSGI server.

Install:

```bash
pip install gunicorn
```

Run:

```bash
gunicorn project.wsgi
```

---

# Nginx

Used as:

- Reverse proxy
- Load balancer
- Static file server

---

# Static File Deployment

Collect static files:

```bash
python manage.py collectstatic
```

---

# Environment Configuration

Manage:

- SECRET_KEY
- Database URLs
- API keys
- Cloud credentials

Use:

- django-environ
- python-decouple

---

# Docker with Django

Containerize Django applications.

Architecture:

```
Django Container

+

PostgreSQL Container

+

Redis Container

+

Worker Container
```

---

# Dockerfile Example

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY .

CMD [
"gunicorn",
"project.wsgi"
]
```

---

# Docker Compose Django

Manage services:

```
web

database

redis

celery-worker

celery-beat
```

---

# Kubernetes Django Deployment

Understand:

- Pods
- Services
- Deployments
- ConfigMaps
- Secrets

---

# Django Scaling

Scale applications using:

- Horizontal scaling
- Load balancing
- Database optimization
- Caching
- Background workers

---

# Load Balancing

Architecture:

```
Users

 |

Load Balancer

 |

----------------

Django Instance 1

Django Instance 2

Django Instance 3

----------------

 |

Database
```

---

# Database Scaling

Strategies:

- Read replicas
- Connection pooling
- Query optimization
- Database partitioning

---

# Django Microservices

Use Django for:

- Independent services
- Business modules
- API platforms

Architecture:

```
API Gateway

 |

----------------

User Service

Order Service

Payment Service

----------------
```

---

# Django AI Integration

Use Django for AI-powered applications.

Examples:

- AI chatbots
- Recommendation systems
- Document processing
- Automation platforms

---

# AI Libraries Integration

Use:

- LangChain
- OpenAI SDK
- Transformers
- PyTorch
- TensorFlow

---

# Django AI Architecture

```
User

 |

Django API

 |

AI Service Layer

 |

LLM Model

 |

Response
```

---

# Django AI Agent Development

Build AI agents with:

- LangChain
- LangGraph
- CrewAI
- AutoGen

---

# Django AI Agent Responsibilities

Agent should:

- Understand user intent
- Call required tools
- Manage workflows
- Store memory
- Return useful responses

---

# Django AI Agent Rules

The Django AI agent must always:

1. Follow Django best practices.

2. Use MVT architecture.

3. Keep business logic separated.

4. Use service layers for complex logic.

5. Validate all inputs.

6. Secure authentication systems.

7. Protect sensitive information.

8. Write reusable applications.

9. Include testing strategies.

10. Optimize database queries.

11. Consider scalability.

12. Create production-ready solutions.

---

# Django Expert Mindset

Think like:

- Senior Django Engineer
- Backend Architect
- API Developer
- Security Engineer
- Cloud Engineer

Build Django systems that are:

- Secure
- Scalable
- Maintainable
- High performance
- Production ready

---

# Django Production Checklist

Before deployment:

## Code Quality

- Clean architecture
- Tests completed
- Documentation available

## Security

- HTTPS enabled
- Secrets protected
- Dependencies updated

## Performance

- Queries optimized
- Cache enabled
- Monitoring configured

## Deployment

- Docker ready
- CI/CD configured
- Logs available

---
