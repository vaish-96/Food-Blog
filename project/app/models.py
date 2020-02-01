from django.db import models

# Create your models here.
class Items(models.Model):
    food_image = models.ImageField()
    item_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)