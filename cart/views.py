from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Products

# Create your views here.
def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    total = 0
    
    for idx,cart_item in cart.items():
        total = total + cart_item['price']
        print (cart_item)
        
    return render(request, 'cart/view_cart.html', {
        'shopping_cart':cart,
        'total':total
    })


def add_cart(request, products_id):
    cart = request.session.get('shopping_cart', {})
    products = get_object_or_404(Products, pk=products_id)
    if products_id not in cart:
        
        cart[products_id] = {
            'id':products_id,
            'name': products.name,
            'price': products.price,
            'quantity':1,
            'image_url':products.image.cdn_url
        }
        
        request.session['shopping_cart'] = cart
        
        messages.success(request, 'Product successfully added to your cart!')
        return redirect('/products/')
    else:
        # cart[products_id]['quantity']+=1
        # cart[products_id]['total']=round(int(cart[products_id]['quantity'])*float(cart[products_id]['price']),2)
        # request.session['shopping-cart'] = cart
        return redirect('/cart/')
        
        
def remove_cart(request, products_id):
    cart=request.session.get('shopping_cart', {})
    
    if products_id in cart:
        del cart[products_id]
        request.session['shopping_cart'] = cart
        messages.success(request, "Product successfully removed from cart!")
    
    return redirect('/cart/')
        
