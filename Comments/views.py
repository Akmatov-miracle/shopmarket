from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions

from Comments import serializers
from Comments.models import Comment
from Comments.permissions import IsOwnerOrReadOnly
from Products.models import Product
from Products.serializers import ProductCommentSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


