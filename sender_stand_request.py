# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data


# Определение функции post_new_order для отправки POST-запроса на создание нового заказа
def post_new_order(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)


# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data

order_response = post_new_order(data.order_body)


# Запрос на получение заказа по треку заказа
def get_order(track_order):
    return requests.get(configuration.URL_SERVICE+configuration.PUT_ORDER,
                        params=track_order)