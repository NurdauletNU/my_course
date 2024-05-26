from django.core.signals import request_finished
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {'title': 'Home - Главная', 
               'content': 'Главная страница магазина - HOME',
               'bool': True,
               'str': 'Привет!'}
    
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About Page')