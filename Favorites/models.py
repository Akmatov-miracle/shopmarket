from django.db import models

# Create your models here.
from Accounts.serializers import User
from Products.models import Product


class Favorites(models.Model):
    author = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites')
    favorites = models.BooleanField()

    class Meta:
        unique_together = ['author', 'product']
        verbose_name = 'favorites'  # пишет в единственном числе
        verbose_name_plural = 'favorites'  # пишет во множественном числе

