import requests
import json
import time
import re

print('setup: cleaning the database')
response = requests.get('http://localhost:8081/api/products/', headers=headers)
items = json.loads(response.text)
item_ids = []
for item in items:
	url = 'http://localhost:8081/api/products//' + str(item['id'])
	print('deleting item ' + str(item['id']))
	r = requests.delete(url, data=json.dumps(item_ids), headers=headers)
	if r.status_code == 200:
		print('ok')
print('starting replay')
