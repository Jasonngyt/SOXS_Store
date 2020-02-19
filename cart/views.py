from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Import the Products model from the products app
from products.models import Products



def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    total = 0
    
    # Calculate and display total price
    for idx,cart_item in cart.items():
        total = total + cart_item['price']
        print (cart_item)
        
    return render(request, 'cart/view_cart.html', {
        'shopping_cart':cart,
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
        print(cart[products_id]['quantity'])
        total = round(cart[products_id]['quantity']*float(cart[products_id]['price']),2)
        # cart[products_id]['total']=round(int(cart[products_id]['quantity'])*float(cart[products_id]['price']),2)
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
        
