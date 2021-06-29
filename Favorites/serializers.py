from rest_framework import serializers

from Favorites.models import Favorites


class FavoritesSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Favorites
        fields = ('product', 'favorites', 'author',)