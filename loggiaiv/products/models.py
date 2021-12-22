from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    imageUrl = models.CharField(max_length=2083)

class discountCode(models.Model):
    code = models.CharField(max_length=8)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    

