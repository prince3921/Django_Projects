Here’s a **clear, step-by-step way to install Django using Conda** (recommended if you’re using Anaconda/Miniconda).

---

## 1️⃣ Open Terminal / Anaconda Prompt

Check conda is installed:

```bash
conda --version
```

---

## 2️⃣ Create a New Conda Environment (Best Practice)

```bash
conda create -n django_env python=3.11
```

Activate it:

```bash
conda activate django_env
```

---

## 3️⃣ Install Django Using Conda

### ✅ Recommended (conda-forge)

```bash
conda install -c conda-forge django
```

Verify installation:

```bash
django-admin --version
```

---



## 5️⃣ Create Django Project (Test Install)

```bash
django-admin startproject myproject
cd myproject
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

---

## 6️⃣ Common Conda + Django Commands

| Task              | Command                            |
| ----------------- | ---------------------------------- |
| List environments | `conda env list`                   |
| Activate env      | `conda activate django_env`        |
| Deactivate env    | `conda deactivate`                 |
| Remove env        | `conda remove -n django_env --all` |
| Check Django      | `django-admin --version`           |

---



## ✅ Best Practice

* Use **one conda env per project**
* Prefer **conda-forge**
* Use `pip` only after activating conda env

---

If you want, I can help you with:

* Django + PostgreSQL setup
* Django REST Framework install
* Django project structure explained
* Django for beginners roadmap

Just tell me 😊

## Summary
conda install in your system
conda through steps to create env
conda through activate env (conda activate envname)
conda install django (conda-forge)
verify django install (django-admin --version)
create django project (django-admin startproject projectname)
run django server(python manage.py runserver)


### folder structure of django
mainproject/
    manage.py
    mainproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    app/
        __init__.py
        views.py
        urls.py
    templates/
        website/
            index.html
    static/
        style.css   




mainproject
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

### setup static and template files
```py
# settings.py
import os
# Add this line to specify template directories
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

```html
templates/website/index.html
<!-- index.html -->
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"> 
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django with Conda</title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
</head>
<body>
    <h1>Welcome to Django with Conda!</h1>
</body>
</html>
```
```css
static/style.css
/* style.css */
body {
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
}
h1 {
    color: #333;
    text-align: center;
    margin-top: 20%;
}
```

summary
setup static and template files in django project
manage.py ke level par static and templates folder bnao
static folder me css file bnao
templates folder me html file bnao
html file me static files ko load kro
css links me static files ka path do

mainproject/settings.py me static and template files ka path add kro
TEMPLATES me DIRS me templates folder ka path do
STATICFILES_DIRS me static folder ka path do
mainproject/views.py me html file ko render kro


