"""
URL configuration for mainproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

# Define the URL patterns for the app
# localhost:8000/app/post
# localhost:8000/app/user/id
urlpatterns = [
    path('', views.app_home, name='app-home'),
    path('login/', views.login, name='login'),
    path('chai/<int:chai_id>/', views.chai_details, name='chai-details'),
]
