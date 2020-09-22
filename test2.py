import requests
import json
import csv
from bs4 import BeautifulSoup

#=================================================================
#MSNから株価を取得test
# 吉野家ＨＬＤＧ株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-9861/fi-a9j1fr"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_yosinoya = int(temp.replace(",",""))
print(kabuka_yosinoya)

# ビックカメラ株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-3048/fi-a9c2lh"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_biccamera = int(temp.replace(",",""))
print(kabuka_biccamera)

# フジ日本精糖株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-2114/fi-a9b7mw"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_fnihonseitou = int(temp.replace(",",""))
print(kabuka_fnihonseitou)

# イオン株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-8267/fi-a9ho6h"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_aeon = int(temp.replace(",",""))
print(kabuka_aeon)

# 飯田グループHLDG株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-3291/fi-a9cf6h"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_iida = int(temp.replace(",",""))
print(kabuka_iida)

# タカラレーベン株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-8897/fi-a9i53m"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_takaraleben = int(temp.replace(",",""))
print(kabuka_takaraleben)

# グローセル株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-9995/fi-a9j72w"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_glosel = int(temp.replace(",",""))
print(kabuka_glosel)

# スカイラークHLDG株価
load_url_msn = "https://www.msn.com/ja-jp/money/stockdetails/tks-3197/fi-a9car7"
html = requests.get(load_url_msn)
soup = BeautifulSoup(html.content, "html.parser")
topstories = soup.find("span", class_="currentval")
temp = topstories.text
kabuka_skylark = int(temp.replace(",",""))
print(kabuka_skylark)
