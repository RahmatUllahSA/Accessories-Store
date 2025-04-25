from django.shortcuts import render
#from django.http import HttpResponse  # 1 Home app'
from .models import Product  # 2 templates


# Create your views here.
def home(request):                      # 1 Home app
    #return HttpResponse('Home')         # 1 Home app
    products = Product.objects.all()  # 2 templates
    return render(request, 'home/home.html', {'products' : products})  # 2 templates
