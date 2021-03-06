import requests
import sys
from datetime import datetime

api_key='0153d4ab127d8086b11ca42f21bb5b3a'
location=input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temperature_city = ((api_data['main']['temp'])-273.15)
weather_description = api_data['weather'][0]['description']
humidity = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time=datetime.now().strftime("%d %b %Y | %I:%M")

print("___________________________________________________________")
print("Weather Stats for - {} || {}".format(location.upper(), date_time))

print("Current temperature is   : {:.2f} deg C".format(temperature_city))
print("Current weather desc     : ",weather_description)
print("Current Humidity         : ",humidity,'%')
print("Current Wind Speed       : ",wind_speed,'kmph')

sys.stdout = open("WeatherAPI.txt","w")

print("___________________________________________________________")
print("Weather Stats for - {} || {}".format(location.upper(), date_time))

print("Current temperature is   : {:.2f} deg C".format(temperature_city))
print("Current weather desc     : ",weather_description)
print("Current Humidity         : ",humidity,'%')
print("Current Wind Speed       : ",wind_speed,'kmph')


sys.stdout.close() 
