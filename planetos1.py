import requests
import json
import csv

# 'noaa_gfs_global_sflux_0.12d”は気象データのID
url = 'http://api.planetos.com/v1/datasets/noaa_gfs_global_sflux_0.12d/point'

#↓後で調べる
querystring = {
    'lat':'35.70',                  #緯度
    'lon':'139.80',                 #経度
    'var':'Temperature_surface',    #温度(絶対温度)
    'count':'1',                   #データ取得数
    'apikey':'09c42ac4bf04441baeca7dfbc69c5ffc' #アカウントで取得したAPIキー
}

#↓後で調べる
response = requests.get(url,params=querystring)
print(response.text)    #.textで取得data表示はできる

#jsonデータで取得
r = requests.get(url,params=querystring)
weather_data = r.json()

#緯度を取得してみる
latitude = weather_data['entries'][0]['axes']['latitude']
print(latitude)

#timeminを取得してみる
timeMin = weather_data['stats']['timeMin']
print(timeMin)

#csvに保存
f = open('tstt_csv','w')
writer = csv.writer(f)
writer.writerow([latitude,timeMin,'テスト'])   #配列です
f.close()
