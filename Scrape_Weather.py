# Openweathermap.org
# https://openweathermap.org/price
# 1,0000 API calls per day for free
import requests
import macos_keychain

# API_KEY = "Your_API_Key"
API_KEY = macos_keychain.get(name="API_KEY_OPENWEATHERMAPORG")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

print('')
city = input("Enter a city name: ")

# Using an F String
# print(f"{BASE_URL}?appid={API_KEY_OPENWEATHERMAPORG}&q={city}")

get_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(get_url)
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("_" * 60)
    print("Weather:", weather)
    celsius = round(data["main"]["temp"] - 273.15, 2)
    fahrenheit = (celsius * 1.8 + 32)
    degree_sign = u'\N{DEGREE SIGN}'
    print(f"Temperature: ", celsius, degree_sign, "C, ", fahrenheit, degree_sign, "F", sep='')
    country = data["sys"]["country"]
    print("Country:", country)
    print("_" * 60)
else:
    print("http code 200 not received. An error occurred.")
