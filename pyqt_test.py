from binance.client import Client
import pprint

api = {
    'api_key' : 'kShelbMozw975QVjLBab0TyDrc079ttlxrXVpCOjBYdd9Dh56WvX5w1Qa7at7Ndj',
    'api_secret': '9Ksh3kGeksXikcMvFvz80jhAwlqDT0KvrlRNShwgzNExYgJC04NXDH8l3sYujhy0'
}

client = Client(api_key = api.get("api_key"), api_secret = api.get("api_secret"))

tickers = client.get_ticker()
pprint.pprint(tickers[0]['symbol'])