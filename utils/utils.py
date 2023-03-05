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


def get_filtered_data(data):
    """function to get filtered data"""
    data = [x for x in data if "state" in x and x["state"] == 'EXECUTED']
    return data


def get_last_data(data, count_last_values):
    """function sorted by date and get last data"""
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:count_last_values]


def get_formatted_data(data):
    """function to get formatted data"""
    formatted_data = []
    for row in data:
        print(row)
        return