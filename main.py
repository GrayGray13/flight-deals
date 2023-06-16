import requests
import os
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
kiwi_endpoint = "https://api.tequila.kiwi.com/v2/search"
KIWI_API_KEY = os.environ['KIWI_API_KEY']
FLY_FROM = "ATL"
FLY_TO = "MCO"
DATE_FROM = "15/06/2023"
DATE_TO = "15/09/2023"
CURRENCY = "USD"

params = {
    'fly_from': FLY_FROM,
    'fly_to': FLY_TO,
    'date_from': DATE_FROM,
    'date_to': DATE_TO,
    'curr': CURRENCY
}

headers = {
    'apikey': KIWI_API_KEY
}
response = requests.get(url=kiwi_endpoint, params=params, headers=headers)

print(response.json())
