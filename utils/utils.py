import requests
from datetime import datetime


def get_data(url):
    """function to get data from url"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "INFO: Данные получены успешно!"
        return None, f"WARNING: Статус ответа {response.status_code}"
    except requests.exceptions.ConnectionError:
        return None, "ERROR: Ошибка соединения с сервером"


def get_filtered_data(data, filtered_empty_from=False):
    """function to get filtered data"""
    data = [x for x in data if "state" in x and x["state"] == 'EXECUTED']
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_data(data, count_last_values):
    """function sorted by date and get last data"""
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:count_last_values]


def get_formatted_data(data):
    """function to get formatted data"""
    formatted_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]

        sender = row["from"].split()
        sender_bill = sender.pop(-1)  # separate bill from name card
        sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]} ** **** {sender_bill[-4:]}"
        sender_info = " ".join(sender)  # join list to string

        recipient = f"**{row['to'][-4:]}"
        amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'
        formatted_data.append(f"""\
{date} {description} 
{sender_info} {sender_bill}  -> Счет {recipient} 
{amount}
""")
    return formatted_data