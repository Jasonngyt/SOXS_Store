from django.shortcuts import render, redirect, reverse, get_object_or_404
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
    
    
def update_products(request, products_id):
    products_being_updated = get_object_or_404(Products, pk=products_id)
    
    if request.method == "POST":
        update_products_form = ProductForm(request.POST, instance=products_being_updated)
        if update_products_form.is_valid():
            update_products_form.save()
         
            return redirect(reverse(show_products))
    else:
        update_products_form = ProductForm(instance=products_being_updated)
    
    return render(request, 'products/update_item.html',{
        'form':update_products_form
    })

def delete_products(request, products_id):
    products_being_deleted = get_object_or_404(Products, pk=products_id)
    return render(request, 'products/delete_item.html', {
        'products':products_being_deleted
    })
    
def confirm_delete_products(request, products_id):
    products_being_deleted = get_object_or_404(Products, pk=products_id)
    products_being_deleted.delete()
    return redirect(reverse('show_products'))