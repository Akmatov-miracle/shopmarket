from django.db import models

from Accounts.serializers import User
from Products.models import Product


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField()

    class Meta:
        unique_together = ['author', 'product']
