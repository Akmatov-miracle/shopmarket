from django.http import HttpResponse
from Products.models import Product
from rest_framework import generics, serializers
from Like.serializers import LikeSerializers


class LikeView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = LikeSerializers


def add_like(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(id=int(pk))
        product.likes += 1
        product.save()
    else:
        raise serializers.ValidationError("HTTP Error 405: Method Not Allowed")
    return HttpResponse("Спасибо за лайк")


def add_dislike(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(id=int(pk))
        product.dislikes += 1
        product.save()
    else:
        raise serializers.ValidationError("HTTP Error 405: Method Not Allowed")
    return HttpResponse("Жалко было лайк поставить?")
