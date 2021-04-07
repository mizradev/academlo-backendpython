import requests
import json

url = 'https://reqres.in/api/users'

response = requests.get(url)
data = response.json()
data_update = {}

total_pages = data['total_pages']

for page in range(total_pages):
	res = requests.get(f'{url}?page={page+1}')
	jsonFile = res.json()
	users = jsonFile['data']
	for user in users:
		data_update[user["email"]] = user	


print(json.dumps(data_update, indent=4))

