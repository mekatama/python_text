import requests
import json

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

#data = json.loads( response.text )

#jsonデータで取得
r = requests.get(url,params=querystring)
weather_data = r.json()

#緯度を取得してみる
latitude = weather_data['entries'][0]['axes']['latitude']
print(latitude)

#timeminを取得してみる
timeMin = weather_data['stats']['timeMin']
print(timeMin)
