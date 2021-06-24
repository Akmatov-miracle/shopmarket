from django.db import models

import Category
from Products import serializers


class Products(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.children.exists():
            representation['children'] = CategorySerializer(instance=instance.children.all(), many=True).data
        return representation
