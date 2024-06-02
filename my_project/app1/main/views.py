from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    
    context = {
               'title': 'Home - Главная', 
               'content': 'Магазина мебели HOME'
               
               }
    
    return render(request, 'main/index.html', context)


def about(request):
    context = {'title': 'Home - О нас', 
               'content': 'О нас',
               'text_on_page': "Добро пожаловать в наш магазин! Мы рады приветствовать вас в нашем мебельном магазине, где стиль, качество и комфорт объединяются, чтобы сделать ваш дом уютным и красивым."
               }
    
    return render(request, 'main/about.html', context)


def contact_info(request):
    return render(request, 'main/contact_info.html')