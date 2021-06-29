from rest_framework import serializers

from Like.models import Like


class LikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Like
        fields = ('product', 'like', 'author',)
