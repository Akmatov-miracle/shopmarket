from django.db import models
from Accounts.serializers import User
from Products.models import Product


class Cart(models.Model):
    author = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart')
    cart = models.BooleanField()

    class Meta:
        unique_together = ['author', 'product']

