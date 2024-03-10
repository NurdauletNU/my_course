import re
import sqlite3
from typing import Any


def execute_sqlite3(database: str, query: str, kwargs={}) -> list[Any]:
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        cursor.execute(query, kwargs)
        connection.commit()
        return cursor.fetchall()


create_table = """
CREATE TABLE IF NOT EXISTS Token (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER UNIQUE,
token TEXT UNIQUE,
created_at TEXT
);
"""

create_user_table = """
CREATE TABLE IF NOT EXISTS User (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE,
password TEXT
);
"""
insert_into_user = """
INSERT INTO User (username, password) VALUES ("Nurik1993", "Qfr43nCvwc")
"""
delete_from_user = """
DELETE FROM User WHERE id=1"""

try:
    execute_sqlite3(database=r"D:\my_course\book_store\backend\token.db", query=create_table)
    execute_sqlite3(database=r"D:\my_course\book_store\backend\token.db", query=create_user_table)
    # execute_sqlite3(database=r"D:\my_course\book_store\backend\token.db", query=insert_into_user)
    # execute_sqlite3(database=r"D:\my_course\book_store\backend\token.db", query=delete_from_user)
    print("Databases created and added successfully")
except Exception as error:
    print("error:", error)


pattern_password = r"^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{10,}$"
pattern_username = r"^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{6,}$"


def check_password(password: str) -> bool:
    return True if re.match(pattern_password, password) else False


def check_username(username: str) -> bool:
    return True if re.match(pattern_username, username) else False
