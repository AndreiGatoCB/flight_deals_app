from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/e0a1becc9118cc374f77b11f81d73d38/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/e0a1becc9118cc374f77b11f81d73d38/flightDeals/users"
TOKEN = "#9UJQI!s1yL6)y"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.mails_data = {}
        self.headers = {
            'Authorization': f'Bearer {TOKEN}',
            "Content-Type": "application/json",
        }

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self.headers)
        data = response.json()
        self.mails_data = data["users"]
        return self.mails_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
