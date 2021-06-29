from rest_framework import generics, permissions

from Cart import serializers
from Cart.models import Cart
from Comments.permissions import IsOwnerOrReadOnly


class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerializer


class CartCreateView(generics.CreateAPIView):
    serializer_class = serializers.CartSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CartDeleteView(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
