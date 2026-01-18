from django.shortcuts import render
from .models import ChaiVariety

# Create your views here.
def app_home(request):
    chais=ChaiVariety.objects.all()
    return render(request, 'app/all_app.html',{'chais':chais})
def register(request):
    return render(request, 'app/register.html')
def login(request):
    return render(request, 'app/login.html')