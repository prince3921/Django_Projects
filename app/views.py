from django.shortcuts import render

# Create your views here.
def app_home(request):
    return render(request, 'app/all_app.html')
def register(request):
    return render(request, 'app/register.html')
def login(request):
    return render(request, 'app/login.html')