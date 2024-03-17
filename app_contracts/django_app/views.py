from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django_app import models, serializers
from django_app.serializers import ContractSerializer


@api_view(http_method_names=["POST", "GET"])
@permission_classes([AllowAny])
def api(request):
    return Response(data={"message": "Hello World"})


@api_view(http_method_names=["POST", "GET"])
@permission_classes([AllowAny])
def get_contract(request):
    contracts = models.Contract.objects.all()
    _serializers = serializers.ContractSerializer(contracts, many=True)
    return Response(data={"message": _serializers.data})
