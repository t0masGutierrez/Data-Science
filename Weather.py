# API Connection
import requests
url = "http://api.openweathermap.org/data/2.5/forecast?"
key = "4b4ee3244032ef1b6bfc8333dc2c428e"
city = "Houston"
test = url + "appid=" + key + "&q=" + city

# Temperature Conversion
def kelvinToFahrenheit(kelvin):
  celsius = kelvin - 273.15
  fahrenheit = celsius * (9/5) + 32
  return fahrenheit

# Get Temperature
response = requests.get(test).json()
tempKelvin = response['list'][0]['main']['temp']
tempFahrenheit = kelvinToFahrenheit(tempKelvin)

# Output
print(f"{city} is currently {tempFahrenheit:0.2f} degrees Fahrenheit")
