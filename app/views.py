from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def app_home(request):
    chais=ChaiVariety.objects.all()
    return render(request, 'app/all_chai.html',{'chais':chais})
def chai_details(request, chai_id):
    chai_details=get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'app/chai_details.html', {'chaidetails': chai_details})
def login(request):
    return render(request, 'app/login.html')