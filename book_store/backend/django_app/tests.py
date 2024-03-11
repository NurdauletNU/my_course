from django.test import TestCase
import requests


# Create your tests here.
def tests():
    token = ""
    try:
        response = requests.get("http://127.0.0.1:8000/user/list/")
        print(response, response.status_code)
        print(response.json())
        if response.status_code != 200:
            raise Exception("456")
    except Exception as error:
        print("успех")

    try:
        data = {"username": "Nurik932", "password": "Qfr43nCvwc"}
        response = requests.post("http://127.0.0.1:8000/api/tokens/", data=data)
        print(response, response.status_code)
        print(response.json())
        if response.status_code != 200:
            raise Exception("456")
    except Exception as error:
        print("УСПЕХ токена на неправильного")

    try:
        data = {"username": "Nurik93", "password": "Qfr43nCvwc"}
        response = requests.post("http://127.0.0.1:8000/api/tokens/", data=data)
        print(response, response.status_code)
        print(response.json())
        print("УСПЕХ токена на правильного")
        if response.status_code != 200:
            raise Exception("456")
        token = response.json().get("token")
    except Exception as error:
        print("ПРОВАЛ токена на правильного")

    try:
        response = requests.get(f"http://127.0.0.1:8000/api/tokens/check?token={token}")
        print(response, response.status_code)
        if response.status_code == 200:
            print("Успешно check")
    except Exception as error:
        print("Ошибка check")


tests()
