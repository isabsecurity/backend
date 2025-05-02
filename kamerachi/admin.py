# Register your models here.
from django.contrib import admin
from django.utils.html import format_html
from .models import *
from django.contrib.auth.models import Group,User
admin.site.register(Category)
admin.site.site_header = 'E-Commerce Admin'


class ImageProductsInline(admin.TabularInline):
    model = ImageProducts
    extra = 1


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "product_image")
    inlines = [ImageProductsInline]

    def product_image(self, obj):
        first_image = obj.images.first()
        if first_image and first_image.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;" />',
                               first_image.image.url)
        return "No Image"

    product_image.short_description = "Rasm:"

class ImagePostsInline(admin.TabularInline):
    model = ImagePosts
    extra = 1


class PostsAdmin(admin.ModelAdmin):
    list_display = ("title", "post_image")
    inlines = [ImagePostsInline]

    def post_image(self, obj):
        first_image = obj.images.first()
        if first_image and first_image.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;" />',
                               first_image.image.url)
        return "No Image"

    post_image.short_description = "Rasm:"




admin.site.register(Order)

admin.site.register(Products, ProductsAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)