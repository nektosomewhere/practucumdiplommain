# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data


def test_get_order_by_track_success():
    """
    Автотест для проверки успешного получения заказа по трекеру.
    """
    # Создание нового заказа
    order_response = sender_stand_request.post_new_order()

    # Извлечение трекера из ответа
    track = order_response.json().get("track")

    # Установка трекера в параметры запроса
    data.params_get["t"] = track

    # Получение заказа по трекеру
    order_get_response = sender_stand_request.get_order(data.params_get)

    # Проверка успешного получения заказа
    assert order_get_response.status_code == 200
