from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# @method_decorator(csrf_protect, name='dispatch')  # CSRF protection for POST requests
@method_decorator(csrf_exempt, name='dispatch')  # CSRF protection for POST requests


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

def index(request):
    """Render an HTML view for products."""
    products = Product.objects.all()
    return render(request, 'inventory/index.html', {'products': products})

class UpdateStockView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        try:
            product = Product.objects.get(id=product_id)
            if product.stock >= quantity:
                product.stock -= quantity
                product.save()
                return Response({"message": "Stock updated successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Insufficient stock"}, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
def csrf_token_view(request):
    return JsonResponse({"message": "CSRF token view is working!"})

#CRUD FUNCTIONS

# Create Product
class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
# Optionally, you can override methods to handle GET requests, or simply not include any
    def get(self, request, *args, **kwargs):
        return Response({"message": "POST request is expected for creating a product."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
# List all products
class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Retrieve a single product
class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Update Product
class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def put(self, request, *args, **kwargs):
        # Allow partial updates if needed
        return super().put(request, *args, **kwargs)

# Delete Product
class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response({"message": "Product deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
