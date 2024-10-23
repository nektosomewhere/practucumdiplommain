# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data


def post_new_order():
    """
    Функция для создания нового заказа.
    Возвращает объект ответа от сервера.
    """
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER,
        json=data.order_body
    )
    return response


def get_order(params):
    """
    Функция для получения заказа по трекеру.
    Принимает словарь параметров запроса.
    Возвращает объект ответа от сервера.
    """
    response = requests.get(
        configuration.URL_SERVICE + configuration.PUT_ORDER,
        params=params
    )
    return response
