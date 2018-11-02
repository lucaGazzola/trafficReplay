import requests
import json
import time
import re
from bson.json_util import loads 
import os.path

headers={'Content-type': 'application/json', 'Accept': 'application/json'}

print('sending authenticate request to http://localhost:8080/api/authenticate')
json_content = {"username":"admin","password":"admin"}
response = requests.post('http://localhost:8080/api/authenticate', data=json.dumps(json_content), headers=headers)
if response.status_code == 200:
	print('authenticated')

content = re.sub(r'"id".*?(?=,)', '"id":None', response.content.decode('utf-8'))
data = loads(content)
file = open('Token.txt','w')
file.write(data['id_token'])
file.close()
