import requests
import matplotlib.pyplot as plt
import pandas as pd
import datetime

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30&interval=daily"
response = requests.get(url)
data = response.json()


market_cap_data = [(datetime.datetime.fromtimestamp(item[0]/1000).strftime('%Y-%m-%d'), item[1]) for item in data["market_caps"]]
