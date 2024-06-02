from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Products, Cart
from django.views.decorators.csrf import csrf_exempt

def cart_add(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)

    if not request.session.session_key:
        request.session.create()

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
        # messages.success(request, "Товар успешно добавлен в корзину.")
    else:
        carts = Cart.objects.filter(session_key=request.session.session_key, product=product)

        if carts.exists():
            cart = carts.first()
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)
        # messages.success(request, "Товар успешно добавлен в корзину.")

    return redirect(request.META.get('HTTP_REFERER', '/'))

    


    
def cart_change(request, product_slug):
    ...
    
   

            
def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])