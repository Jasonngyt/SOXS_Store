from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields=('name', 'material', 'size', 'price', 'stock', 'category')