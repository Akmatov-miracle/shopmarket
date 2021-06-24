from rest_framework import mixins, viewsets

from Products import serializers
from Products.models import ProductImages


class ProductImageViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = serializers.ProductImageSerializer
    queryset = ProductImages.objects.all()
