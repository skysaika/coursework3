import requests


def get_data(url):
    """function to get data from url"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "INFO: Данные получены успешно!"
        return None, f"WARNING: Статус ответа {response.status_code}"
    except requests.exceptions.ConnectionError:
        return None, "ERROR: Ошибка соединения с сервером"

