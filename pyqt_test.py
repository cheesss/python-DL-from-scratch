# from binance.client import Client
# import pprint

# api = {
#     'api_key' : 'kShelbMozw975QVjLBab0TyDrc079ttlxrXVpCOjBYdd9Dh56WvX5w1Qa7at7Ndj',
#     'api_secret': '9Ksh3kGeksXikcMvFvz80jhAwlqDT0KvrlRNShwgzNExYgJC04NXDH8l3sYujhy0'
# }

# client = Client(api_key = api.get("api_key"), api_secret = api.get("api_secret"))

# tickers = client.get_ticker()
# pprint.pprint(tickers[0]['symbol'])


import asyncio
import websockets
import json

msg = \
{
  "jsonrpc" : "2.0",
  "id" : 9929,
  "method" : "public/auth",
  "params" : {
    "grant_type" : "client_credentials",
    "client_id" : "gayC-1T7",
    "client_secret" : "rjdp0DpSGoae0cUlydtC73GYSs4Qio7sLVJvEaHlFbk"
  }
}

async def call_api(msg):
   async with websockets.connect('wss://www.deribit.com/ws/api/v2') as websocket:
       await websocket.send(msg)
       while websocket.open:
           response = await websocket.recv()
           # do something with the response...
           print(response)

asyncio.get_event_loop().run_until_complete(call_api(json.dumps(msg)))