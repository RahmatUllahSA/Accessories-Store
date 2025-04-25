# new file created that name is urls.py

from django.urls import path  # Home app
from . import views  # Home app

urlpatterns = [
    path('',views.home, name= 'home'),  #  1 Home app
     path('category/<str:category_name>/', views.category_products, name='category_products'),  # 3 category
]