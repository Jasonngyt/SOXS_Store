from django import forms
from .models import Products, Category
from pyuploadcare.dj.forms import ImageField

class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields=('name', 'material', 'size', 'price', 'category', 'image')

class ProductsSearch(forms.Form):
    search_terms = forms.CharField(required=False)
    min_price = forms.FloatField(required=False, min_value=0.0)
    max_price = forms.FloatField(required=False)