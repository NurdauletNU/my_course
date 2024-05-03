import datetime
from functools import wraps

from django.http import JsonResponse, HttpRequest


class Decorators:
    @staticmethod
    def dec_error_handle(func: callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as error:
                return JsonResponse(data={'message': str(error)}, status=500)

        return wrapper

    @staticmethod
    def constr_def_logger(is_class: bool = False):
        def dec_logger(func: callable):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if is_class:
                    _request: HttpRequest = args[1].path if len(args) > 1 else None
                else:
                    _request: HttpRequest = args[0].path if isinstance(args[0], HttpRequest) else None

                datetime_str = datetime.datetime.now().strftime("%Y_%m_%d_%H")
                with open(f"static/media/log_{datetime_str}.txt", "a") as f:
                    if _request:
                        f.write(f"{str(datetime.datetime.now())} _ {_request}\n")
                    else:
                        f.write(f"{str(datetime.datetime.now())} _ No HttpRequest object found\n")
                result = func(*args, **kwargs)
                return result

            return wrapper

        return dec_logger


class Datetime:
    @staticmethod
    def get_current_datetime():
        return datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")

# Декоратор @wraps в Python является частью модуля functools и используется для
# сохранения метаданных функции после её декорирования.
# Это важно, потому что декорирование функции может изменить её атрибуты,
# такие как имя, документацию и другие атрибуты,
# что может привести к нежелательным эффектам в коде,
# особенно при использовании отладочных инструментов или рефлексии.
