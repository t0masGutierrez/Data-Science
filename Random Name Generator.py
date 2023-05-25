import requests
response = requests.get("https://randomuser.me/api")

firstName = response.json()['results'][0]['name']['first']
lastName = response.json()['results'][0]['name']['last']

print("Name - " + firstName + " " + lastName)