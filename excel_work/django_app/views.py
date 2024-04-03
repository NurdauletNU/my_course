from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_app import models
from datetime import datetime


@api_view(http_method_names=["GET"])
# http://127.0.0.1:8000/?param_date_from=2024-03-01&param_date_to=2024-04-01
# {'2024-03-01': {"Юбилейный": Decimal('106000.00')}, '2024-03-17': Decimal('45000.00'),
# '2024-04-01': Decimal('27000.00')}
# {'2024-03-01': {'Юбилейный': Decimal('34000.00'), 'Умка': Decimal('72000.00')},
# '2024-03-17': {'Юбилейный': Decimal('45000.00')},
# '2024-04-01': {'Юбилейный': Decimal('27000.00')}}
# [(1, datetime.date(2024, 3, 1), 'Юбилейный', 10, 2000, 'Сладости'),
# (2, datetime.date(2024, 3, 17), 'Юбилейный', 15, 3000, 'Хлебобулочные'),
# (3, datetime.date(2024, 4, 1), 'Юбилейный', 18, 1500, 'Другое'),
# (4, datetime.date(2024, 3, 1), 'Умка', 18, 1500, 'Сладости'),
# (5, datetime.date(2024, 3, 1), 'Умка', 15, 3000, 'Хлебобулочные'),
# (6, datetime.date(2024, 3, 1), 'Юбилейный', 7, 2000, 'Сладости')]
def home(request):
    param_date_from_str = request.GET.get("param_date_from")
    param_date_from = datetime.strptime(param_date_from_str, "%Y-%m-%d").date()
    param_date_from_formatted = param_date_from.strftime("%Y-%m-%d")
    param_date_to_str = request.GET.get("param_date_to")
    param_date_to = datetime.strptime(param_date_to_str, "%Y-%m-%d").date()
    param_date_to_formatted = param_date_to.strftime("%Y-%m-%d")

    cursor = connection.cursor()
    query = f"""
    SELECT  month, shop, category, SUM(count*price) 
    FROM django_app_products
    WHERE month BETWEEN '{param_date_from_formatted}' 
    AND '{param_date_to_formatted}'
    GROUP BY month, shop, category
    """
    cursor.execute(query)
    data = cursor.fetchall()
    print(query)
    print(data)
    for i in data:
        print(i)

    # filter_date = (models.Products.objects.filter(month__gte=param_date_from_formatted).
    #                filter(month__lte=param_date_to_formatted))
    # data = {}
    # for i in filter_date:
    #     month_key = str(i.month)
    #     shop_key = str(i.shop)
    #     category_key = str(i.category)
    #     if month_key not in data:
    #         data[month_key] = {}
    #     if shop_key not in data:
    #         data[month_key][shop_key] = {}
    #     if category_key not in data:
    #         data[month_key][shop_key][category_key] = 0
    #     old_total_price = (
    #         data.get(month_key, {}).get(shop_key, {}).get(category_key, 0))
    #     data[month_key][shop_key][category_key] = old_total_price + i.price * i.count
    #
    # data_2 = []
    return Response(data={'message': data})
