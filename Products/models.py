from django.db import models

import Category


class Products(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        if not self.parent:
            return f'{self.name}'
        else:
            return f'{self.parent} ---> {self.name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'