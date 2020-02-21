from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Import the Products model from the products app
from products.models import Products



def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    subtotal = 0
    total = 0
    
    # Calculate and display total price
    for idx,cart_item in cart.items():
        subtotal = cart[idx]['price']*cart[idx]['quantity']
        total = total + subtotal
        print (cart_item)
    
    return render(request, 'cart/view_cart.html', {
        'shopping_cart':cart,
        'subtotal':subtotal,
        'total':total
    })



def add_cart(request, products_id):
    
    # get the object specified by the key 'shopping_cart', if not found, return an empty dictionary
    cart = request.session.get('shopping_cart', {})
    
    # Add the products specified by the products_id argument to cart
    products = get_object_or_404(Products, pk=products_id)
    if products_id not in cart:
        
        cart[products_id] = {
            'id':products_id,
            'name': products.name,
            'price': products.price,
            'quantity':1,
            'image_url':products.image.cdn_url
        }
        
        # save the cart back to the session under the key 'shopping_cart'
        request.session['shopping_cart'] = cart
        
        messages.success(request, 'Product successfully added to your cart!')
        return redirect('/products/')
    else:
        cart[products_id]['quantity']+=1
        request.session['shopping-cart'] = cart
        return redirect('/products/')
        
        
# Increase the quantity of the socks in the cart        
def add_quantity(request, products_id):
    
    # get the object specified by the key 'shopping_cart', if not found, return an empty dictionary
    cart = request.session.get('shopping_cart', {})
    
    # Add the products specified by the products_id argument to cart
    products = get_object_or_404(Products, pk=products_id)

    cart[products_id]['quantity']+=1
    request.session['shopping-cart'] = cart
    return redirect('/cart/')

# Decrease the quantity of the socks in the cart 
def minus_quantity(request, products_id):
    
    # get the object specified by the key 'shopping_cart', if not found, return an empty dictionary
    cart = request.session.get('shopping_cart', {})
    
    # Add the products specified by the products_id argument to cart
    products = get_object_or_404(Products, pk=products_id)
    
    # check and prevent the quantity drop less than 1
    if cart[products_id]['quantity'] > 1:
        cart[products_id]['quantity']-=1
    
    request.session['shopping-cart'] = cart
    return redirect('/cart/')
    
        
def remove_cart(request, products_id):
    cart=request.session.get('shopping_cart', {})
    
    # Remove the products specified by the products_id argument to cart
    if products_id in cart:
        del cart[products_id]
        request.session['shopping_cart'] = cart
        messages.success(request, "Product successfully removed from cart!")
    
    return redirect('/cart/')
        
