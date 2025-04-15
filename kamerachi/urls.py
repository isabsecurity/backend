from django.urls import path
from kamerachi.views import *

urlpatterns = [
    path("categories/", CategoryListAPIView.as_view()),
    path("products/<int:category_id>/", ProductListAPIView.as_view()),
    path("products/", ProductListAPIView.as_view()),
    path("product-details/<int:product_id>/", ProductDetailsAPIView.as_view()),
    path("posts/", PostsListAPIView.as_view()),
    path("posts/<int:category_id>/", PostsListAPIView.as_view()),
    path("posts-details/<int:post_id>/", PostsDetailsAPIView.as_view()),
    path("popular-products/", PopularProducts.as_view()),
    path("create-order/", OrderCreateAPIView.as_view()),
]
