from django.shortcuts import render
#from django.http import HttpResponse  # 1 Home app'
from .models import Product  # 2 templates


# Create your views here.
def home(request):                      # 1 Home app
    #return HttpResponse('Home')         # 1 Home app
    products = Product.objects.all()  # 2 templates
    return render(request, 'home/home.html', {'products' : products})  # 2 templates

def category_products(request, category_name):  # 3 category 
    # ক্যাটাগরি অনুযায়ী প্রোডাক্ট টাইপ ফিল্টার করুন
    products = {                                     # 3 category 
        'earbuds': ['Xiaomi', 'UBL', 'JBL'],      # 3 category 
        'headphones': ['Headphone 1', 'Headphone 2', 'Headphone 3'],   # 3 category 
        'airbuds': ['Airbud 1', 'Airbud 2', 'Airbud 3'],          # 3 category 
        'smartwatch': ['Smart Watch 1', 'Smart Watch 2'],       # 3 category 
        'pendrive': ['Pendrive 1', 'Pendrive 2'],               # 3 category 
        'computerbox': ['Computer Box 1', 'Computer Box 2'],    # 3 category 
        'mouse': ['Mouse 1', 'Mouse 2'],                        # 3 category 
        'keyboard': ['Keyboard 1', 'Keyboard 2'],                # 3 category 
    }
    product_list = products.get(category_name, [])              # 3 category 
    return render(request, 'home/category_products.html', {'category_name': category_name, 'product_list': product_list}) # 3 category 