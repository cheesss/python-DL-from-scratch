import pybithumb
import time
import datetime

con_key= "3588f3caa5b757bb8071c9a2bd4443c6"
sec_key= "2cff6acf43cf1f68ee7fcecedbc1b588"

bithumb = pybithumb.Bithumb(con_key,sec_key)

balance = bithumb.get_balance("BTC")

# while True:
#     price = pybithumb.get_current_price("BTC")
#     print(price)
#     time.sleep(0.2)
# 비트코인 가격 0.2초마다 호출하기

df = pybithumb.get_ohlcv("BTC")
# # print(df.tail())
# yesterday = df.iloc[-2]
# today_open = yesterday['close']
# yesterday_high = yesterday['high']
# yesterday_low = yesterday['low']
# target = today_open + (yesterday_high - yesterday_low) * 0.5
# print(target)

def get_target_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
target_price = get_target_price("BTC")

while True:
    now = datetime.datetime.now()
    if mid < now < mid + datetime.timedelta(seconds=10) :
        target_price = get_target_price("BTC")
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

    current_price = pybithumb.get_current_price("BTC")
    print(current_price)

    time.sleep(1)