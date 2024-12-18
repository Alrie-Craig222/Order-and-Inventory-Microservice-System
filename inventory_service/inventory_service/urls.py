"""
URL configuration for inventory_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views  # Import the views from the current app
from django.http import HttpResponse
from django.shortcuts import render  # Import render for template rendering


def home(request):
    # return HttpResponse("Welcome to the Home Page!")
     return render(request, "index.html")  # Render the index.html file

# Define URL patterns for the inventory service
urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    # path('inventory/', views.index, name='inventory'),  # Correct the path to refer to inventory_home
     path('inventory/', include('inventory.urls')),  # Delegate inventory URLs to the app
     
]

