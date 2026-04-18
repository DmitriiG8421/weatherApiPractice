import requests

url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(url)
print(response)

data = response.json()
print(data['message'])