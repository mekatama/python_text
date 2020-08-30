import requests
import json
import csv

# Alpha Vantageの為替データ
# response01 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo')
# print(response.text)    #.textで取得data表示はできる

# Alpha Vantageの為替データ jsonデータで取得
#USD
r01 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=9C61LRH22KOSAPQO')
kawase_data01 = r01.json()

#EUR
r02 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=JPY&apikey=9C61LRH22KOSAPQO')
kawase_data02 = r02.json()

#AUD
r03 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=AUD&to_currency=JPY&apikey=9C61LRH22KOSAPQO')
kawase_data03 = r03.json()


#USD取得
usd = kawase_data01['Realtime Currency Exchange Rate']['5. Exchange Rate']
print(usd)

#EUR取得
EUR = kawase_data02['Realtime Currency Exchange Rate']['5. Exchange Rate']
print(EUR)

#AUD取得
aud = kawase_data03['Realtime Currency Exchange Rate']['5. Exchange Rate']
print(aud)
