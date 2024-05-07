from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
         'content': 'Главная страница магазина - HOME',
         'list': ['first', 'second'],
         'dict': {'first':1},
         'is_authenticated':True
    }
    return render(request, 'django_app/index.html', context=context)

def about(request):
    return HttpResponse('About Page')