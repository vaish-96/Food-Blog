from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Items(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$')
    author = models.CharField(max_length=255)
    user = models.IntegerField(default=1)
    profile_pic = models.ImageField(upload_to='Profile_pic',blank=True)
    item_name = models.CharField(max_length=255)
    servings = models.IntegerField(default=1)
    preparation_time =models.CharField(max_length=255,validators=[alphanumeric],default="1 Min")
    cooking_time = models.CharField(max_length=255,validators=[alphanumeric],default="1 Min")
    food_image = models.ImageField(upload_to='food_pic',blank=True)
    ingredients = models.TextField(max_length=None,validators=[alphanumeric],default="Text Here")
    direction = models.TextField(max_length=None,validators=[alphanumeric],default="Text Here")
    item_type = models.CharField(max_length=255)

    def __str__(self):
        return self.item_name

class Items_List(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    item_list = models.ForeignKey(Items,on_delete=models.CASCADE)