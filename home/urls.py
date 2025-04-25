# new file created that name is urls.py

from django.urls import path  # Home app
from . import views  # Home app

urlpatterns = [
    path('',views.home, name= 'home'),  # Home app
]