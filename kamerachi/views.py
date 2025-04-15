from django.shortcuts import  get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class CategoryPagination(PageNumberPagination):
    page_size = 100


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination

    def get_queryset(self):
        return Category.objects.all()





class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        queryset = Products.objects.prefetch_related("images")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class ProductDetailsAPIView(generics.RetrieveAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

    def get_object(self):
        product_id = self.kwargs.get("product_id")
        return get_object_or_404(Products, pk=product_id)


class PostsListAPIView(generics.ListAPIView):
    serializer_class = PostsSerializer

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        queryset = Posts.objects.prefetch_related("images")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class PostsDetailsAPIView(generics.RetrieveAPIView):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()

    def get_object(self):
        post_id = self.kwargs.get("post_id")
        return get_object_or_404(Posts, pk=post_id)


class PopularProducts(APIView):
    serializer_class = ProductsSerializer

    def get(self, request):
        popular_products = Products.objects.order_by("-created_at")[:8]
        serializer = self.serializer_class(popular_products, many=True, context={'request': request})
        return Response(serializer.data)


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
