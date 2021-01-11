from django.db import models
from django.utils.text import slugify


class AboutProduct(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    item_name = models.CharField(max_length=50)
    discription = models.TextField()
    available_size = models.CharField(max_length=255)
    frozen_style = models.CharField(max_length=255)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.item_name



class Certification(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

