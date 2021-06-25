from django.shortcuts import render
from rest_framework import generics

from Favorites.models import Favorite
from Favorites.serializers import FavoriteSerializer


class FavoriteListView(generics.ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        qs = self.request.user.profile_customer
        queryset = Favorite.objects.all()
        return queryset

