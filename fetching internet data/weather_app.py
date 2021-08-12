
# get the weather URL
# give the City as input 
# output should print Weather, Temperature, Humidity, Wind Speed info

import requests
import json 

API_KEY = "6c7b5cdc8b366b3d4ef06f90ca952766"

city_name = input("Enter City Name >  ")
URL = f"api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

res = requests.get(URL)
json_data = json.loads(res.text)

Weather = json_data["weather"][0]["description"]
Temp = json_data["main"]["temp"]
Humidity = json_data["weather"]["description"]
Wind_speed = json_data["main"]["humidity"]

print("Weather: ", Weather)
print("Temperature: ", Temp)
print("Humidity: ", Humidity)
print("Wind Speed: ", Wind_speed)


