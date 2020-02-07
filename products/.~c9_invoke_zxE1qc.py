from django.shortcuts import render, redirect, reverse
from .models import Products
from .forms import ProductForm

# Create your views here.

def show_products(request):
    all_products = Products.objects.all()
    return render(request, 'products/show_item.html', {
        'all_products':all_products
    })

def create_products(request):
    if request.method == 'POST':
        create_products_form = ProductForm(request.POST)
        if create_products_form.is_valid():
            create_products_form.save()
            return redirect(reverse(show_products))
    else:
        create_products_form = ProductForm()
            
    return render(request, 'products/create_item.html', {
        'form':create_products_form
    })
    
