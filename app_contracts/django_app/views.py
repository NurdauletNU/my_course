from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django_app import models, serializers
from django_app.serializers import ContractSerializer, AgentSerializer, CommentSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Contract


@api_view(http_method_names=["POST", "GET"])
@permission_classes([AllowAny])
def api(request):
    return Response(data={"message": "Hello World"})


@api_view(['GET'])
@permission_classes([AllowAny])
def contract_list(request):
    contracts = Contract.objects.all()
    _serializer = ContractSerializer(contracts, many=True)
    return Response(data={"message": _serializer.data})


@api_view(http_method_names=["POST", "GET"])
@permission_classes([AllowAny])
def get_comment(request):
    comments = models.Comment.objects.all()
    _serializers = serializers.CommentSerializer(comments, many=True)
    return Response(data={"message": _serializers.data})


@api_view(http_method_names=["POST", "GET"])
@permission_classes([AllowAny])
def get_agent(request):
    agents = models.Agent.objects.all()
    _serializers = serializers.AgentSerializer(agents, many=True)
    return Response(data={"message": _serializers.data})


@api_view(['GET'])
@permission_classes([AllowAny])
def contract_detail(request, pk):
    try:
        contract = Contract.objects.get(pk=pk)
    except Contract.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    _serializer = ContractSerializer(contract)
    return Response(data={"message": _serializer.data})


@api_view(['POST'])
@permission_classes([AllowAny])
def contract_create(request):
    serializer = ContractSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([AllowAny])
def contract_update(request, pk):
    try:
        contract = Contract.objects.get(pk=pk)
    except Contract.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ContractSerializer(contract, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def contract_delete(request, pk):
    try:
        contract = Contract.objects.get(pk=pk)
    except Contract.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    contract.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_contract_by_author(request, pk):
    try:
        author = User.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(data={"error": "Автор не найден"}, status=status.HTTP_404_NOT_FOUND)

    contract = models.Contract.objects.filter(author=author)
    if not contract.exists():
        return Response(data={"error": "Контракты не найдены для этого автора"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ContractSerializer(contract, many=True)
    total_count = contract.count()
    return Response(data={"message": serializer.data, "total_count": total_count}, status=status.HTTP_200_OK)

