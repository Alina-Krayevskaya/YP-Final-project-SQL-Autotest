import requests
from configuration import URL_SERVICE


def create_order(order_data):
    response = requests.post(f"{URL_SERVICE}/api/v1/orders", json=order_data)
    return response


def get_order_by_track(track_number):
    response = requests.get(f"{URL_SERVICE}/api/v1/orders/track?t={track_number}")
    return response