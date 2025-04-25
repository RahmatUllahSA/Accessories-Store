
from django.contrib import admin
from django.urls import include, path # Home app  # 2 templates


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))  # Home app
    
]
