from utils.utils import get_data


def main():
    DATA_JSON = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678104559111&signature=zWzdiPwc4jR19dH5kXSEDL_-w6jYQ7XBtMj0TqkJUko&downloadName=operations.json"

    data, info = get_data(DATA_JSON)
    if not data:
        exit(info)
    print(info)

    print(data)

if __name__ == '__main__':
    main()
