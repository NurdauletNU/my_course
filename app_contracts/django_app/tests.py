from django.test import TestCase
import psycopg2

conn = psycopg2.connect(dbname='django_db', user='admin', password='admin', host='localhost', port='5432')
cursor = conn.cursor()
cursor.execute('SELECT 1')  # стандартный запрос для postgres
cursor.close()
conn.close()
