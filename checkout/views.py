from django.shortcuts import render, reverse, HttpResponse, get_object_or_404

from django.conf import settings
import stripe

from products.models import Products

from django.views.decorators.csrf import csrf_exempt

endpoint_secret = 'whsec_ySyA8VU4jKYPv6M4WJG7xJCOUFoZPkj6'

# Create your views here.

def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    cart = request.session.get('shopping_cart', {})
    
    line_items = []
    for id, products in cart.items():
        products = get_object_or_404(Products, pk=id)
        line_items.append({
            'name' : products.name,
            'amount': int(products.price * 100),
            'currency' : 'usd',
            'quantity' : 1
        })
      
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        success_url=request.build_absolute_uri(reverse(checkout_success)),
        cancel_url=request.build_absolute_uri(reverse(checkout_cancelled)),
    )
    print(settings.STRIPE_PUBLISHABLE_KEY)  
    return render(request, 'checkout/checkout.html',{
        'session_id' : session.id,
        'public_key' : settings.STRIPE_PUBLISHABLE_KEY
    })

def checkout_success(request):
    request.session['shopping_cart'] = {}
    return render(request, 'checkout/thankyou.html')
    
def checkout_cancelled(request):
    return HttpResponse("Checkout cancelled")
    
@csrf_exempt
def payment_completed(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
        
    if event['type'] == 'checkout.session.completed':
        session =event['data']['object']
        
        handle_checkout_session(session)
    
    return HttpResponse(status=200)

def handle_checkout_session(session):
     print(session)