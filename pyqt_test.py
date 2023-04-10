import requests
import json

endpoint = "https://api.binance.com/api/v3/ticker/24hr"
symbol = "BTCUSDT"

response = requests.get(endpoint, params={'symbol': symbol})

if response.status_code == 200:
    data = json.loads(response.text)
    print(f"Symbol: {data['symbol']}, PriceC: {data['priceChange']}")
else:
    print(f"Error: {response.status_code}, {response}")
