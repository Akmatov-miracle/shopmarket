from rest_framework import serializers

from Comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    # post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = ('id', 'body', 'author', 'product')

