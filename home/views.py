from django.shortcuts import render
from django.http import HttpResponse # Home app


# Create your views here.
def home(request):                           # Home app
    return HttpResponse('Home')         # Home app
