from rest_framework import generics, permissions

from Comments.permissions import IsOwnerOrReadOnly
from Favorites.models import Favorites
from Favorites import serializers


class FavoritesListView(generics.ListAPIView):
    queryset = Favorites.objects.all()
    serializer_class = serializers.FavoritesSerializer


class FavoritesCreateView(generics.CreateAPIView):
    serializer_class = serializers.FavoritesSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FavoritesDeleteView(generics.DestroyAPIView):
    queryset = Favorites.objects.all()
    serializer_class = serializers.FavoritesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
