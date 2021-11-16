# settings
path_to_photos = ""
api_key = ""

# wait for computer to get internet connection
import time

# get your location
import geocoder
start = time.time()
def get_location():
   gc = geocoder.ip('me').latlng
   if gc != None:
      return(list(geocoder.ip('me').latlng))
   else:
      end = time.time()
      if end - start > 300:
      # if after 5 minutes we stil cannot reach the api, the weather is set to clear
         return([46.0, 14.5])
      else:
         time.sleep(29)
         return(get_location())
g = get_location()
lat, lon = str(g[0]), str(g[1])

# get current time
from datetime import datetime
now = str(datetime.now())
hour = int(now[11:13])

# extracts time of the day
if hour > 6 and hour < 18: totd = 'day'
else: totd = 'night'

# api call
import requests
start = time.time()
def return_api():
   try:
      response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=' + api_key)
      if response.status_code == 200:
         data = response.json()
         return(data['weather'][0].get('id'))
   except:
      # in case weather api is unreachable, we try again in 30 seconds
      end = time.time()
      if end - start > 180:
         # if after 3 minutes we stil cannot reach the api, the weather is set to clear
         return(800)
      else:
         time.sleep(29)
         return(return_api())
report = return_api()

# weather extraction
if report >= 200 and report < 300: weather='thunderstorm'
elif report >= 300 and report < 600: weather='rain'
elif report >= 600 and report < 700: weather='snow'
elif report >= 700 and report < 800: weather='fog'
elif (report == 800 or report == 801) and totd == 'day': weather='clear'
elif (report == 800 or report == 801) and totd != 'day': weather='clear_night'
else: weather='clouds'

# set background
import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, path_to_photos + '/' + weather + '.jpg' , 0)
