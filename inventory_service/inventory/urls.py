from django.urls import path
from .views import ProductListView, UpdateStockView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView
from .views import csrf_token_view

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('update-stock/', UpdateStockView.as_view(), name='update_stock'),
    path('csrf-token/', csrf_token_view),

    path('products/', ProductListView.as_view(), name='product_list'),  # GET all products
    path('products/create/', ProductCreateView.as_view(), name='product_create'),  # POST to create product
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # GET single product by ID
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),  # PUT/PATCH to update product
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),  # DELETE product by ID
]