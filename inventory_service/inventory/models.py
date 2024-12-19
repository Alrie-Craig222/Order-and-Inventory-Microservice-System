from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    description = models.TextField(default="")  # Add this field for product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Add this field for product price

    def __str__(self):
        return self.name
