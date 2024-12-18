from django.urls import path
from .views import ProductListView, UpdateStockView
from .views import csrf_token_view

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('update-stock/', UpdateStockView.as_view(), name='update_stock'),
    path('csrf-token/', csrf_token_view),
]
