# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data


# Объединенная функция для создания заказа и проверки его статуса
def create_and_check_order():
    # Создание нового заказа
    order_response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                                   json=data.order_body)

    # Проверка успешности создания заказа
    if order_response.status_code == 200:
        # Извлечение трека заказа из ответа
        track_order = order_response.json().get('track')

        # Выполнение GET-запроса для проверки заказа по треку
        get_order_response = requests.get(configuration.URL_SERVICE + configuration.PUT_ORDER,
                                          params={'track': track_order})

        # Проверка успешности получения информации о заказе
        assert get_order_response.status_code == 200, "Order retrieval failed"
        return get_order_response.json()
    else:
        raise Exception(f"Order creation failed with status code: {order_response.status_code}")


# Вызов основной функции автотеста
create_and_check_order()
