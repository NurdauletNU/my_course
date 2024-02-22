from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return JsonResponse(data={"message": "Hello World!"})
