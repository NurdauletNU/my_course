from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_app import models, serializers
import json


def index(request):
    return JsonResponse({"message": "Hello World"})


@api_view(http_method_names=['GET'])
@permission_classes([AllowAny])
def api(request):
    return Response(data={'message': 'OK'})


@api_view(http_method_names=['GET'])
# http://127.0.0.1:8000/api/persons/?sort=id&filter={%22first_name%22:%22%D0%9F%D0%B0%D0%B2%D0%B5%D0%BB%22}
@permission_classes([AllowAny])
def get_persons(request):
    objects = models.Person.objects.all()
    sort = request.GET.get('sort', None)
    if sort:
        objects = objects.order_by(sort)
    filter_ = request.GET.get('filter', None)
    if filter_:
        filter_dict = json.loads(filter_)
        objects = objects.filter(**filter_dict)
    return Response(data={'data': serializers.PersonSerializer(objects, many=True).data})


@api_view(http_method_names=['GET'])
@permission_classes([AllowAny])
def get_person(request, tabel_num: int):
    try:
        object = models.Person.objects.get(tabel_num=tabel_num)
        return Response(data={'data': serializers.PersonSerializer(object, many=False).data})
    except models.Person.DoesNotExist:
        return Response(status=404, data={'error': 'Tabel num not found'})


@api_view(http_method_names=['GET'])
@permission_classes([AllowAny])
def get_categories(request):
    objects = models.ClothCategory.objects.all()
    sort = request.GET.get('sort', None)
    if sort:
        objects = objects.order_by(sort)
    filter_ = request.GET.get('filter', None)
    if filter_:
        filter_dict = json.loads(filter_)
        objects = objects.filter(**filter_dict)
    return Response(data={'data': serializers.ClothCategorySerializer(objects, many=True).data})


@api_view(http_method_names=['GET'])
@permission_classes([AllowAny])
def get_category(request, id):
    try:
        objects = models.ClothCategory.objects.filter(id=id)
        return Response(data={'data': serializers.ClothCategorySerializer(objects, many=True).data})
    except models.ClothCategory.DoesNotExist:
        return Response(status=404, data={'error': 'Category not found'})


@api_view(http_method_names=['GET'])
@permission_classes([AllowAny])
def get_clothes(request):
    objects = models.Cloth.objects.all()
    sort = request.GET.get('sort', None)
    if sort:
        objects = objects.order_by(sort)
    filter_ = request.GET.get('filter', None)
    if filter_:
        filter_dict = json.loads(filter_)
        objects = objects.filter(**filter_dict)
    return Response(data={'data': serializers.ClothSerializer(objects, many=True).data})


@api_view(http_method_names=['GET'])
@permission_classes([AllowAny])
def get_clothes(request, id):
    try:
        objects = models.Cloth.objects.get(id=id)
        return Response(data={'data': serializers.ClothSerializer(objects, many=False).data})
    except models.Cloth.DoesNotExist:
        return Response(status=404, data={'error': 'Cloth not found'})
