from rest_framework import generics
from Products import serializers

from Products.models import Products


class ProductListView(generics.ListAPIView):
    queryset = Products.objects.select_related('category')
    serializer_class = serializers.ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = serializers.ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = serializers.ProductSerializer
