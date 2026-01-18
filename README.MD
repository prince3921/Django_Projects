
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

### Project Structure
```
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




