from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from . import models, serializers
from .models import Book
from django_app import utils


@api_view(["GET"])
def api_users(request: Request) -> Response:
    users_objs = User.objects.all()
    user_json = serializers.UserSerializer(users_objs, many=True).data
    return Response(data={"message": user_json})


@api_view(["GET"])
def api(request: Request) -> Response:
    # book_obj = models.Book.objects.all()[0]   # ручная сериализация
    # book_obj1 = {"id": book_obj.id, "title": book_obj.title, "description": book_obj.description}

    books_obj = models.Book.objects.all()
    book_json = serializers.BookSerializer(instance=books_obj, many=True).data
    return Response(data={"message": book_json})


@api_view(["GET"])
def get_books(request: Request) -> Response:
    sort = request.GET.get("sort", "desc")
    books = Book.objects.all()

    match sort:
        case "name_asc":
            books = books.order_by("title")
        case "name_desc":
            books = books.order_by("-title")
        case _:
            books = books.order_by("title")

    selected_page = request.GET.get(key="page", default=1)
    pages = Paginator(object_list=books, per_page=20)
    page = pages.page(number=selected_page)

    serialized_books = [{"id": x.id, "title": x.title, "description": x.description} for x in page.object_list]
    total_count = len(books)
    return Response({"serialized_books": serialized_books, "total_count": total_count, "sort": sort})


@api_view(["GET"])
@permission_classes([AllowAny])
def api(request: Request) -> Response:
    # book_obj = models.Book.objects.all()[0]   # ручная сериализация
    # book_obj1 = {"id": book_obj.id, "title": book_obj.title, "description": book_obj.description}

    books_obj = models.Book.objects.all()
    book_json = serializers.BookSerializer(instance=books_obj, many=True).data
    return Response(data={"message": book_json})


# @api_view(["GET"])
# def get_book(request: Request, book_id: str) -> Response:
#     book = Book.objects.get(id=int(book_id))
#     serializer_book = {"id": book.id, "title": book.title, "description": book.description}
#     return Response({"data": serializer_book})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_users(request: Request) -> Response:
    return Response(data={"users": "ok"})


@api_view(["POST"])
@permission_classes([AllowAny])
def api_user_register(request: Request) -> Response:
    print("request.data", request.data)
    email = request.data.get("email", None)
    password = request.data.get("password", None)
    if email and password:
        User.objects.create(email=email, password=make_password(password))
        return Response(data={"success": "Account is successfully created"})
    else:
        return Response(data={"error": "email or password is failed"})


"""
{
"username": "Nurik93",
"password": "Qfr43nCvwc"
}
"""


@api_view(http_method_names=["POST"])
def token(request: Request) -> Response:
    username = request.data.get("username", None)
    password = request.data.get("password", None)
    if not utils.check_password(password) or not utils.check_username(username):
        return Response(data={"error": "username or password is invalid"}, status=status.HTTP_401_UNAUTHORIZED)
    user_ = utils.execute_sqlite3(
        database=r"D:\my_course\book_store\backend\token.db",
        query="SELECT id, username FROM User WHERE username = : username AND password = : password",
        kwargs={"username": username, "password": password},
    )
    print(user_)
    return Response(data={"token": "ok"})
