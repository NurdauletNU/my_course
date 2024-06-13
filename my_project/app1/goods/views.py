from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.shortcuts import get_list_or_404, render
from goods.models import Products, Categories
from goods.serializers import CategorySerializer, ProductSerializer
from goods.utils import q_search
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView



def catalog(request, category_slug=None):
    
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)
    
    
    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)
    
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))
        
    
    context = {
        "title": "HOME - Каталог",
        "goods": current_page,
        "slug_url": category_slug
        }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)
    context = {'product': product}
    
    return render(request, "goods/product.html", context)




class CategoryAPIView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        category = Categories.objects.all().values()
        return Response({'category': category})
    
    
    def post(self, request):
        post_new = Categories().objects.create(
            name=request.data['name'],
            slug=request.data['slug'],
            
        )
        return Response({'post': model_to_dict(post_new)})
    
    
    
class ProductAPIIView(APIView):
    permission_classes=[AllowAny]
    
    def get(self, request):
        product = Products.objects.all().values()
        return Response({'prproduct':product})
    
    def post(self, request):
        post_new = Categories().objects.create(
            name=request.data['name'],
            slug=request.data['slug'],
            description=request.data['description'],
            price=request.data['price'],
            discount=request.data['discount'],
            quantity=request.data['quantity'],
            category_id=request.data['category_id'])
        return Response({'post': model_to_dict(post_new)})
    
    

# class CategoryAPIView(generics.ListAPIView):
#    queryset = Categories.objects.all()
#    serializer_class = CategorySerializer
    
# class ProductAPIIView(generics.ListAPIView):
#    queryset = Products.objects.all()
#    serializer_class = ProductSerializer