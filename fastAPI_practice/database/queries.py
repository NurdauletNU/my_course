import psycopg2
from dotenv import load_dotenv
import asyncpg
import os

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')


def get_db_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        dbuser=DB_USER,
        dbpassword=DB_PASSWORD,
        dbhost=DB_HOST,
        dbport=DB_PORT
    )


def get_db_version():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT version():")
    db_version = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return db_version
