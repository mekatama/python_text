import requests
import json
import csv
# フジ日本精糖株価
k03 = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=2114.T&apikey=9C61LRH22KOSAPQO')
k03a = k03.json()
print(k03a)
kabuka_fnihonseitou = k03a['Global Quote']['05. price']
