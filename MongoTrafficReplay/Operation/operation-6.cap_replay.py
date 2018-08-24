import requests
import json
import time
import re
headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImF1dGgiOiJST0xFX0FETUlOLFJPTEVfVVNFUiIsImV4cCI6MTUyNzk1MDQ0Mn0.n4DzZ-0vTGyo4yx9mUP5C9EaNhjCcNXHrAh5DNVrdVuTWSA9p_wu8jsJ2hIaEVTCvvPxNy0OOLbMIIsBrPoFjg'}

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
