import pytest


from utils.utils import get_data, get_last_data, get_formatted_data, get_filtered_data


def test_get_data():
    """test get_data function"""
    url_json = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678104559111&signature=zWzdiPwc4jR19dH5kXSEDL_-w6jYQ7XBtMj0TqkJUko&downloadName=operations.json"
    assert get_data(url_json) is not None  # test if url correct
    url_json = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678104559111&signature=zWzdiPwc4jR19dH5kXSEDL_-w6jYQ7XBtMj0TqkJUko&downloadNam=operations.json"
    data, info = get_data(url_json)
    assert data is None  # test if url incorrect
    assert info == "WARNING: Статус ответа 400"
    url_json = "https://fil.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678104559111&signature=zWzdiPwc4jR19dH5kXSEDL_-w6jYQ7XBtMj0TqkJUko&downloadName=operations.json"
    data, info = get_data(url_json)
    assert data is None  # test if Connection
    assert info == "ERROR: Ошибка соединения с сервером"


def test_get_filtered_data(test_data):
    """test get_filtered_data function"""
    assert len(get_filtered_data(test_data)) == 4  # test if filter correct
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 2



def test_get_last_data(test_data):
    """test get_last_data function"""
    data = get_last_data(test_data, count_last_values=2)
    assert data[0]['date'] == '2021-04-04T23:20:05.206878'
    assert len(data) == 2


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data[:1])  # test if absolute match
    assert data == ['26.08.2019 Перевод организации \nMaestro 1596 83 ** **** 5199  -> Счет **9589 \n31957.58 руб.\n']
    data = get_formatted_data(test_data[3:4])  # test for absence "FROM"
    assert data == ['23.03.2018 Открытие вклада \n[СКРЫТО]   -> Счет **2431 \n48223.05 руб.\n']
