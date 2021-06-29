from Comments.permissions import IsOwnerOrReadOnly
from Like import serializers
from Like.models import Like

from rest_framework import generics, permissions


class LikeListView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer


class LikeCreateView(generics.CreateAPIView):
    serializer_class = serializers.LikeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)