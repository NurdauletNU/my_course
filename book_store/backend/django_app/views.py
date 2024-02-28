from django.contrib.auth.models import User
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from . import models, serializers
from .models import Book


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
