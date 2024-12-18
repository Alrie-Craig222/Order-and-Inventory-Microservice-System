from django.contrib import admin
from django.urls import path, include
from inventory import urls as inventory_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include('order_service.urls')),
    path('inventory/', include('inventory_urls')),
]
