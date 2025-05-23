from django.db import models
import cloudinary.uploader
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_delete
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "1. Kategoriyalar"


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    description_ru=models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Kamera listi"
        verbose_name_plural = "2. Kameralar listi"
    def __str__(self):
        return self.name

class ImageProducts(models.Model):
    product = models.ForeignKey(Products, related_name="images", on_delete=models.CASCADE)
    image = CloudinaryField("image")

    class Meta:
        verbose_name = "Rasm"
        verbose_name_plural = "Rasmlar"

@receiver(post_delete, sender=ImageProducts)
def delete_product_image(sender, instance, **kwargs):
    if instance.image:
        try:
            cloudinary.uploader.destroy(instance.image.public_id)
        except Exception as e:
            print(f"Cloudinary rasm o‘chirishda xatolik: {e}")
class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    service_included=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Buyurtma beruvchi"
        verbose_name_plural = "Buyurtma beruvchilar"
    def __str__(self):
        return self.name

class TelegramAdminsID(models.Model):
    tg_id = models.BigIntegerField()

    def __str__(self):
        return self.tg_id


class Posts(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title=models.CharField(max_length=200)
    title_ru=models.CharField(max_length=200)
    title_en=models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    description_ru=models.TextField(null=True, blank=True)
    description_en=models.TextField(null=True, blank=True)
    class Meta:
        verbose_name = "Post listi"
        verbose_name_plural = "3. Post listi"
    def __str__(self):
        return self.title
class ImagePosts(models.Model):
    post = models.ForeignKey(Posts, related_name="images", on_delete=models.CASCADE)
    image = CloudinaryField("image")

    class Meta:
        verbose_name = "Rasm"
        verbose_name_plural = "Rasmlar"