from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(blank=False, max_length=255)
    material = models.CharField(blank=False, max_length=255)
    size = models.CharField(blank=False, max_length=255)
    price = models.FloatField(blank=False)
    stock = models.IntegerField(blank=False)
    category = models.CharField(blank=False, max_length=255)
    
    def __str__(self):
        return self.name
