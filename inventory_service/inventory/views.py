from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

@method_decorator(csrf_protect, name='dispatch')  # CSRF protection for POST requests
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

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
