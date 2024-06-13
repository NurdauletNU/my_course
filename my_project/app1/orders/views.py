from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carts.models import Cart
from django.forms import model_to_dict
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from orders.serializers import OrderItemSerializer, OrderSerializer


@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            product=cart_item.product
                            name=cart_item.product.name
                            price=cart_item.product.sell_price()
                            quantity=cart_item.quantity


                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                       В наличии - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен!')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('cart:order')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Home - Оформление заказа',
        'form': form,
        'orders': True,
    }
    return render(request, 'orders/create_order.html', context=context)

class OrderAPIView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        order = Order.objects.all().values()
        return Response({'order':order})
    
    def post(self, request):
        post_new = Order().objects.create(
            user=request.data['user'],
            created_timestamp=request.data['created_timestamp'],
            phone_number=request.data['phone_number'],
            requires_delivery=request.data['requires_delivery'],
            delivery_address=request.data['delivery_address'],
            payment_on_get=request.data['payment_on_get'],
            is_paid=request.data['is_paid'],
            status=request.data['status'],
        )
        return Response({'post': model_to_dict(post_new)})
    
class OrderItemAPIView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        order_item = OrderItem.objects.all().values()
        return Response({'order_item':order_item})
    
    def post(self, request):
        post_new = Order().objects.create(
            product=request.data['product'],
            name=request.data['name'],
            price=request.data['price'],
            quantity=request.data['quantity'],
            created_timestamp=request.data['created_timestamp'],
        )
        return Response({'post': model_to_dict(post_new)})
    

# class OrderAPIView(generics.ListAPIView):
#    queryset = Order.objects.all()
#    serializer_class = OrderSerializer
    
    
# class OrderItemAPIView(generics.ListAPIView):
#    queryset = OrderItem.objects.all()
#    serializer_class= OrderItemSerializer