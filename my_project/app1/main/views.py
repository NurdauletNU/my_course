from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories

def index(request):
    categories = Categories.objects.all()
    context = {'title': 'Home - Главная', 
               'content': 'Магазина мебели HOME',
               'categories': categories
               }
    
    return render(request, 'main/index.html', context)


def about(request):
    context = {'title': 'Home - О нас', 
               'content': 'О нас',
               'text_on_page': "Добро пожаловать в наш магазин! Мы рады приветствовать вас в нашем мебельном магазине, где стиль, качество и комфорт объединяются, чтобы сделать ваш дом уютным и красивым."
               }
    
    return render(request, 'main/about.html', context)
