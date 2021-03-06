from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from Accounts.models import CustomUser
from Products.models import Product

User = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}-->{self.product}-->{self.created_at}-{self.body[0:10]}"