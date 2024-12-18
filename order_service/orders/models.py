from django.db import models

class Order(models.Model):
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - Product {self.product_id}"
