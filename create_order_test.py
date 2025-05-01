# Алина Краевская, 29-я когорта — Финальный проект. Инженер по тестированию расширенный
import pytest
from data import order_data  
from sender_stand_request import create_order, get_order_by_track

def test_create_and_get_order():
    # Шаг 1: Создание заказа
    create_response = create_order(order_data)
    
    assert create_response.status_code == 201  # Проверка кода ответа на создание заказа
    
    # Сохранение номера трека заказа
    track_number = create_response.json().get('track')

    # Шаг 2: Получение заказа по треку заказа
    get_response = get_order_by_track(track_number)
    
    # Проверка, что код ответа равен 200
    assert get_response.status_code == 200

if __name__ == '__main__':
    pytest.main()