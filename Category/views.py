
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, serializers, permissions

from Category.models import Category
from Category.serializers import CategorySerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from Category.serializers import CategoryCreateSerializers


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
#
# class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class CategoryCreateView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializers


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
