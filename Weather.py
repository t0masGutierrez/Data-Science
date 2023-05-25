import requests
url = "http://api.openweathermap.org/data/2.5/forecast?"
key = "ed483c3ee33c8fb1be95422824064b36"
city = "Houston"
test = url + "appid=" + key + "&q=" + city

def kelvinToFahrenheit(kelvin):
  celsius = kelvin - 273.15
  fahrenheit = celsius * (9/5) + 32
  return fahrenheit

response = requests.get(test).json()

tempKelvin = response['list'][0]['main']['temp']
tempFahrenheit = kelvinToFahrenheit(tempKelvin)

print(f"temperature in {city} is currently {tempFahrenheit:0.2f} degrees Fahrenheit")