import random
import string
import datetime
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
        query="SELECT id, username FROM User WHERE username = :username AND password = :password",
        kwargs={"username": username, "password": password},
    )
    if len(user_) <= 0:
        return Response(data={"error": "invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    user_id, username = user_[0]
    hash: str = ""
    for _ in range(128):
        hash += random.choice(list(string.ascii_letters + string.digits))
    utils.execute_sqlite3(
        database=r"D:\my_course\book_store\backend\token.db",
        query="INSERT OR REPLACE INTO Token (user_id, token, created_at) VALUES (:user_id, :token, :created_at)",
        kwargs={"user_id": user_id, "token": hash, "created_at": str(datetime.datetime.now())},
    )
    return Response(data={"token": hash})


# @api_view(["GET"])
# def user_list(request: Request) -> Response:
#     token_str = request.query_params.get("token", "")
#     token = utils.execute_sqlite3(
#         database=r"D:\my_course\book_store\backend\token.db",
#         query="SELECT user_id, created_at FROM Token WHERE token = :token",
#         kwargs={"token": token_str},
#     )
#     if len(token) <= 0:
#         return Response(data={"error": "invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
#     user_id, created_at = token[0]
#     created_at = datetime.datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S.%f")
#     print(created_at)
#     return Response(data={"users": []})


def authenticate(func):
    def wrapper(*args, **kwargs):
        request: Request = args[0]
        token_str = request.query_params.get("token", "")

        if not token_str:
            return Response(data={"error": "token is missing"}, status=status.HTTP_401_UNAUTHORIZED)
        token = utils.execute_sqlite3(
            database=r"D:\my_course\book_store\backend\token.db",
            query="SELECT user_id, created_at FROM Token WHERE token = :token",
            kwargs={"token": token_str},
        )
        if not token:
            return Response(data={"error": "invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
        user_id, created_at = token[0]
        created_at = datetime.datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S.%f")
        if (datetime.datetime.now() - datetime.timedelta(minutes=10)) > created_at:
            return Response(data={"error": "token expired"}, status=status.HTTP_401_UNAUTHORIZED)
        user_ = utils.execute_sqlite3(
            database=r"D:\my_course\book_store\backend\token.db",
            query="SELECT  username FROM User WHERE id = :user_id",
            kwargs={"user_id": user_id},
        )
        if not user_:
            return Response(data={"error": "user unknown"}, status=status.HTTP_401_UNAUTHORIZED)
        print(user_)
        request.userextend = user_
        args = (request,)
        res = func(*args, **kwargs)
        return res

    return wrapper


@api_view(http_method_names=["GET"])
@authenticate
def user_list(request: Request) -> Response:
    return Response(data={"data": [request.userextend]})


@api_view(http_method_names=["POST"])
def token_block(request: Request) -> Response:
    token_for_block = request.data.get("token", "")
    utils.execute_sqlite3(
        database=r"D:\my_course\book_store\backend\token.db",
        query="DELETE FROM Token WHERE token = :token_for_block",
        kwargs={"token_for_block": token_for_block},
    )
    return Response(data={"data": "deleted successfully"})


@api_view(http_method_names=["GET"])
@authenticate
def token_verify(request: Request) -> Response:
    return Response(data={"data": "verified successfully"})
