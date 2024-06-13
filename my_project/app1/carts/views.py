from django.forms import model_to_dict
from django.http import JsonResponse
from carts.models import Cart
from carts.serializers import CartSerializer
from goods.models import Products
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Products, Cart
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound

def cart_add(request, product_slug):
    try:
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
                cart = Cart.objects.create(user=request.user, product=product, quantity=1)
            message = "Товар успешно добавлен в корзину."
        else:
            carts = Cart.objects.filter(session_key=request.session.session_key, product=product)

            if carts.exists():
                cart = carts.first()
                cart.quantity += 1
                cart.save()
            else:
                cart = Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)
            message = "Товар успешно добавлен в корзину."

        return JsonResponse({'message': message, 'cart_quantity': cart.quantity})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def cart_change(request, product_slug):
    ...
    

   

            
def cart_remove(request, cart_id):
    try:
        cart = get_object_or_404(Cart, id=cart_id)
        cart.delete()

        response_data = {
            "message": "Товар успешно удален из корзины"
        }

        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)




class CartAPIView(APIView):
    permission_classes = [AllowAny]
    
    
    def get(self, request):
        cart = Cart.objects.all().values()
        return Response({'cart': cart})
    
    def post(self, request):
        post_new = Cart.objects.create(
            user_id=request.data['user_id'],
            product=request.data['request'],
            quantity=request.data['quantity'],
            session_key=request.data['session_key'],
            created_timestamp=request.data['created_timestamp']
        )
        return Response({'post': model_to_dict(post_new)})
    
    
    

# class CartAPIView(generics.ListAPIView):
#        queryset = Cart.objects.all()
#        serializer_class = CartSerializer
        
    