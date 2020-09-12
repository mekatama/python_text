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
    usd = kawase_data01['Realtime Currency Exchange Rate']['5. Exchange Rate']
    print(usd)

#AUD
    r03 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=AUD&to_currency=JPY&apikey=9C61LRH22KOSAPQO')
    kawase_data03 = r03.json()
    aud = kawase_data03['Realtime Currency Exchange Rate']['5. Exchange Rate']
    print(aud)

#EUR
    r02 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=JPY&apikey=9C61LRH22KOSAPQO')
    kawase_data02 = r02.json()
    eur = kawase_data02['Realtime Currency Exchange Rate']['5. Exchange Rate']
    print(eur)


#csvに保存
    f = open('keizai_csv','w')
    writer = csv.writer(f)
    writer.writerow([usd,aud,eur])   #配列です
    f.close()
