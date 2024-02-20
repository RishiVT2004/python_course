import requests
import json

city = input("enter name of city : ")

url = f'https://api.weatherapi.com/v1/current.json?key=c06ce7e7849143a7a1b75631241202&q={city}'
r = requests.get(url)

# The requests module in Python is used for making HTTP requests to web servers
# request.get() -> fetches the url
# r.text is string in nature
# json module has a function json.loads which loads a string and convert it to dic/list

w_dic = json.loads(r.text)
# r.text = reads the given url

# s_list = json.loads(r.text)

print(f'local time : {w_dic["location"]["localtime"]}')
print(f'location : {w_dic["location"]["region"]}')
print(f'country : {w_dic["location"]["country"]}')
print(f'temp in celcius : {w_dic["current"]["temp_c"]}')
print(f'temp in fahrenheit : {w_dic["current"]["temp_f"]}')
print(f'wind speed : {w_dic["current"]["wind_kph"]} km/ph')
print(f'humidity : {w_dic["current"]["humidity"]} % ')

# print(f'temp in cel : {s_list["current"]["temp_c"]}')
