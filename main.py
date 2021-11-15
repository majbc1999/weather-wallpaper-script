# wait for computer to get internet connection
import time
time.sleep(30)

# get your location
import geocoder
g = list(geocoder.ip('me').latlng)
lat, lon = str(g[0]), str(g[1])

# gets current date and time
from datetime import datetime
time = str(datetime.now())
month = time[5:7]
hour = int(time[11:13])

# extracts season and time of the day
if month == '01' or month == '12' or month == '02': season = 'winter'
elif month == '03' or month == '04' or month == '05': season = 'spring'
elif month == '06' or month == '07' or month == '08': season = 'summer'
else: season = 'autumn'
if hour > 6 and hour < 18: totd = 'day'
else: totd = 'night'

# api call
from requests import get
from secrets import api_key
response = get('https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=' + api_key)
if response.status_code == 200:
   data = response.json()
   report = data['weather'][0].get('id') # dictionary with current weather data
else:
   report = 800

# weather extraction
if report == 800: weather = 'clear'
elif report > 800: weather = 'cloudy'
elif report > 600: weather = 'snowwy'
else: weather = 'rainy'

# set background
import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, 'C:/Users/majbc/OneDrive/Dokumenti/weather-background-script/photos/'+ season + '/' +  totd + '/' + weather + '.jpg' , 0)
