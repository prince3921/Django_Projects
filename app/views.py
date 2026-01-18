from django.shortcuts import render

# Create your views here.

def all_posts(request):
    return render(request, 'app/all_app.html')
def order_posts(request):
    return render(request, 'app/order.html')