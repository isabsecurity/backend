from rest_framework import serializers
from django.contrib.auth import get_user_model
from decouple import config
from .models import *
User = get_user_model()


class ImageProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProducts
        fields = ["image"]
class ImagePostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePosts
        fields = ["image"]

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name']

    def get_name(self, obj):
        request = self.context.get("request")
        lang = request.query_params.get("lang") if request else None

        if lang == "ru":
            return obj.name_ru
        elif lang == "en":
            return obj.name_en
        return obj.name

class SubCategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = SubCategory
        fields = ['id', 'name']

    def get_name(self, obj):
        request = self.context.get("request")
        lang = request.query_params.get("lang") if request else None

        if lang == "ru":
            return obj.name_ru
        elif lang == "en":
            return obj.name_en
        return obj.name

class ProductsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    videos = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = [
            "id", "name", "images",'videos' "description",
             "category"
        ]


    def get_name(self, obj):
        request = self.context.get("request")
        lang = request.query_params.get("lang") if request else None

        if lang == "ru":
            return obj.name_ru
        elif lang == "en":
            return obj.name_en
        return obj.name

    def get_description(self, obj):
        request = self.context.get("request")
        lang = request.query_params.get("lang") if request else None

        if lang == "ru":
            return obj.description_ru
        elif lang == "en":
            return obj.description_en
        return obj.description

    def get_images(self, obj):
        return [
            self._make_https(img.image.url)
            for img in obj.images.all()
        ]
    def get_videos(self, obj):
        return [
            self._make_https(video.video.url)
            for video in obj.videos.all()
        ]

    def _make_https(self, url):
        if url.startswith("http://"):
            return url.replace("http://", "https://")
        return url


class PostsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = [
            "id", "name", "images", "description",
             "category"
        ]


    def get_name(self, obj):
        request = self.context.get("request")
        lang = request.query_params.get("lang") if request else None

        if lang == "ru":
            return obj.name_ru
        elif lang == "en":
            return obj.name_en
        return obj.name

    def get_description(self, obj):
        request = self.context.get("request")
        lang = request.query_params.get("lang") if request else None

        if lang == "ru":
            return obj.description_ru
        elif lang == "en":
            return obj.description_en
        return obj.description

    def get_images(self, obj):
        return [
            self._make_https(img.image.url)
            for img in obj.images.all()
        ]

    def _make_https(self, url):
        if url.startswith("http://"):
            return url.replace("http://", "https://")
        return url


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields ='__all__'

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        order.save()
        return order



