from django.db import models

# Create your models here.
class Items(models.Model):
    item_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)