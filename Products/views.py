from django.http import Http404
from rest_framework import generics, serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import serializers


from Products.models import Product
# from .serializers import PaginationPost


@api_view(['GET'])
def api_overview_links(request):
    print(request.build_absolute_uri())
    urls = {
        'Admin_site': 'admin/',
        'List_site': 'posts/List/',
        'create_site': 'posts/create/',
        'detail_site': 'posts/<int:pk>/detail/',
        'Update_site': 'posts/<int:pk>/update/',
        'delete_site': 'posts/<int:pk>/delete/',
    }
    for key in urls:
        urls[key] = request.build_absolute_uri() + urls[key]
    return Response(urls)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    # pagination_class = PaginationPost


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    @api_view(['DELETE'])
    def task_delete(request, pk):
        try:
            task = Product.objects.get(id=pk)
            task.delete()
            return Response("Task deleted successfully", status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist as error:
            raise Http404


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


# class LikeListView(generics.ListAPIView):
#     queryset = Like.objects.all()
#     serializer_class = serializers.LikeSerializer
#
#
#     @action(detail=True, methods=['post'])
#     def Like(self, request, pk=None):
#         product = self.get_object()
#         obj, created = Like.objects.get_or_create(user=request.user.profile_customer)
#         if not created:
#             obj.like = not obj.like
#             obj.save()
#         liked_or_unliked = 'like' if obj.like else 'unliked'
#         return Response('Successfully {} post'.format(liked_or_unliked), product, status=status)

