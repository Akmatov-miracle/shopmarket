from ckeditor.fields import RichTextField
from django.db import models
from Category.models import Category


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255)
    # decimal_places - цифры после зяпятой
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = RichTextField()
    quantity = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # like = models.PositiveIntegerField(default=0)
    # dislike = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return self.title

      
class ProductImages(models.Model):
    image = models.ImageField(upload_to='products', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
