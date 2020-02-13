from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Products(models.Model):
    name = models.CharField(blank=False, max_length=255)
    material = models.CharField(blank=False, max_length=255)
    size = models.CharField(blank=False, max_length=255)
    price = models.FloatField(blank=False)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    
    image = ImageField(null=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(blank=False, max_length=100)
    
    def __str__(self):
        return self.category