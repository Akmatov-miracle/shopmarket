from rest_framework import serializers

from Cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Cart
        fields = ('product', 'cart', 'author',)
