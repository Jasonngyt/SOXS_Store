from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Products

# Create your views here.
def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    
    return render(request, 'cart/view_cart.html', {
        'shopping_cart':cart
    })

def add_cart(request, products_id):
    
    cart = request.session.get('shopping_cart', {})
    products = get_object_or_404(Products, pk=products_id)
    if products_id not in cart:
        
        cart[products_id] = {
            'id':products_id,
            'name': products.name,
            'price': products.price
        }
        
        request.session['shopping_cart'] = cart
        
        messages.success(request, 'Product successfully added to your cart!')
        return redirect('/products/')
    else:
        return redirect('/products/')
        
def remove_cart(request, products_id):
    cart=request.session.get('shopping_cart', {})
    
    if products_id in cart:
        del cart[products_id]
        request.session['shopping_cart'] = cart
        messages.success(request, "Product successfully removed from cart!")
    
    return redirect('/products/')
        
