from django import forms
from .models import Products, Category
from pyuploadcare.dj.forms import ImageField

class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields=('name', 'material', 'size', 'price', 'stock', 'category', 'image')