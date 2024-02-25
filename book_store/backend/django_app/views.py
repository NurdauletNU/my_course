from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Book


def index(request):
    return JsonResponse(data={"message": "Hello World!"})


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
def get_book(request: Request, book_id: str) -> Response:
    book = Book.objects.get(id=int(book_id))
    serializer_book = {"id": book.id, "title": book.title, "description": book.description}
    return Response({"data": serializer_book})


# class BookListAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     pagination_class = None
#
#     def get_queryset(self):
#         page = self.request.query_params.get("page")
#         page_size = self.request.query_params.get("pageSize", 10)
#         if page:
#             start_index = (int(page) - 1) * int(page_size)
#             end_index = start_index + int(page_size)
#             return Book.objects.all()[start_index:end_index]
#         return Book.objects.all()
