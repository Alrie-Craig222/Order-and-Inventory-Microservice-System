# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Welcome to the Inventory Service!")


# from django.shortcuts import render
# from .models import Product  # Assuming the model is named Product

# def index(request):
#     # Retrieve all products from the database
#     products = Product.objects.all()
    
#     # Pass the products to the template for rendering
#     return render(request, 'inventory/index.html', {'products': products})
