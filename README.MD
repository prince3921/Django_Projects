
### Django Project
This is a Django project that serves as a web application framework for building web applications quickly and efficiently. It follows the Model-View-Template (MVT) architectural pattern and provides a robust set of tools and libraries to facilitate web development.
### Features
- User authentication and authorization
- Admin interface for managing application data
- ORM (Object-Relational Mapping) for database interactions
- Templating engine for rendering HTML pages
- Form handling and validation
- Middleware support for request/response processing
- Built-in security features to protect against common web vulnerabilities

### django commands
```bash
# Create a new Django project
django-admin startproject myproject 

# run the development server
python manage.py runserver

# Create a new Django app
python manage.py startapp app

# Apply database migrations
python manage.py migrate

### Project Structure
```plaintext
myproject/
│├── manage.py
│├── myproject/
││   ├── __init__.py
││   ├── settings.py
││   ├── urls.py
││   └── wsgi.py
│├── app/
││   ├── __init__.py
││   ├── views.py
││   └── urls.py
│├── templates/
││   └── website/
││       └── index.html
│└── static/
│    └── style.css
```


### setup static and template files
```py
# templates/website/index.html
<!-- index.html -->
{% load static %}
<!DOCTYPE html> html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{% static 'style.css' %}">
    <title>Django Project</title>
</head>
<body>
    <h1>Welcome to the Django Project!</h1>
</body>
</html>
```

### template file settings
```py
# settings.py
import os
# Add this line to specify template directories
TEMPLATES = [
    {
        ...,
        'DIRS': ['templates'],
        ...,
    },
]

```
```css
# static/style.css
/* style.css */
body {
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;     
    margin: 0;
    padding: 0;
}
h1 {
    color: #333;
    text-align: center; 
    margin-top: 20%;
}
``` 
### static files settings
```py
# settings.py
import os
# Add this line to specify template directories
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

### views and urls
```py
# views.py
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, Django with Conda!")
def about(request):
    return HttpResponse("About Page")
def contact(request):
    return HttpResponse("Contact Page") 

# urls.py
from django.urls import path
from .views import home, about, contact
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
```

### app creation
```bash
# Create a new Django app
python manage.py startapp app
```
### settings.py modification
```py
# settings.py
# Add 'app' to the INSTALLED_APPS list
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

```
### mainproject urls.py transfer to app urls.py 
```py
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views   
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('app/', include('app.urls')),  # Include app URLs
]
```

```py
# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),  # New URL pattern for post view
]
```

### layout of jinja template
```html
<!-- templates/website/base.html -->
{% load static %}
<!DOCTYPE html> html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{% static 'stylesheets/home.css' %}">
    <title>{% block title %}Django Project{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="{% url 'home' %}">Home</a>
        <a href="{% url 'about' %}">About</a>
        <a href="{% url 'contact' %}">Contact</a>
    </nav>
    <div class="content">
        {% block content %}
        {% endblock %}
    </div>      

</body>
</html>
```
### extending base template
```html
<!-- templates/website/index.html -->
{% extends 'website/base.html' %}
{% block title %}Home - Django Project{% endblock %}
{% block content %}
    <h1>Welcome to the Django Project!</h1>     
{% endblock %}
```

### Apply database migrations
apply : admin, auth, contenttypes, sessions
```bash 
python manage.py migrate
```

### create admin userpassword(superuser)
```bash
python manage.py createsuperuser

prince
prince@@7061

```
### reset superuser password
```bash
python manage.py changepassword <username>
```

### Tailwind CSS Integration

[Setup_Tailwind CSS_Flowbite](https://flowbite.com/docs/getting-started/django/)


### database setup in django with sqlite3
```py
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
### database setup in django with postgresql
```py
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Pillow installation for image handling
```bash
python -m pip install Pillow
```

### Media files settings
```py
# settings.py
import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### mainproject urls.py modification for media files
```py
# mainproject/urls.py
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    ...
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
``` 

# make migrations for media files
```bash
python manage.py makemigrations appname
python manage.py migrate
```



### command to run tests
```bash
python manage.py runserver
npm run dev
```