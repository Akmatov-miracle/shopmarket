from rest_framework import serializers

from Category.serializers import CategorySerializer
from Comments.serializers import CommentSerializer
from Like.serializers import LikeSerializer
from Products.models import Product, ProductImages


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        # print(validated_data)
        request = self.context.get('request')
        # print("Файлы: ", request.FILES)
        images_data = request.FILES
        created_product = Product.objects.create(**validated_data)
        print(created_product)
        print("Work", images_data.getlist('image'))
        print("is not work: ", images_data)
        # for image_data in images_data.getlist('images'):
        #     PostImages.objects.create(post=created_post, image=image_data)
        images_obj = [
            ProductImages(product=created_product, image=image) for image in images_data.getlist('image')
        ]
        ProductImages.objects.bulk_create(images_obj)
        return created_product

    def to_representation(self, instance):  # он отвечает за то в каком виде возвращается Response
        representation = super().to_representation(
            instance)  # подтягиваем родительский метод и добавляем свою переменную
        #  и так в instance  сейчас хранится Product,  чтобы вытащить все картинки этого поста
        # мы можем обратиться через related_name = 'images'  типа Product.images.all()

        representation['images'] = ProductImageSerializer(instance.images.all(), many=True, context=self.context).data
        # representation2['feedbacks'] = FeedbackSerializer(instance.feedbacks.all(), many=True,
        # context=self.context).data
        return representation



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation

class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title')

    def to_representation(self, instance):
        representation = super().to_representation(
            instance)
        representation['comments'] = CommentSerializer(instance.comments.all(), many=True,
                                                         context=self.context).data
        return representation