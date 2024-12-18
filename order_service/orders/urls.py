from django.urls import path
from .views import CreateOrderView, OrderDetailView
from .views import csrf_token_view

urlpatterns = [
    path('create/', CreateOrderView.as_view(), name='create_order'),
    path('<int:order_id>/', OrderDetailView.as_view(), name='order_detail'),
    path('csrf-token/', csrf_token_view),
]
