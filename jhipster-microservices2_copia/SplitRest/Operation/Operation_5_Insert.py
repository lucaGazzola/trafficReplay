import requests
import json
import time
import re
from bson.json_util import loads 
import os.path

id_dict = {}
print('sending post request to http://localhost:8081/api/products/')
json_content = {"name":"prod3","price":33.35}
print(str(json_content))
response = requests.post('http://localhost:8081/api/products/', data=json.dumps(json_content), headers=headers)
if response.status_code == 201:
	print('created')

cont = loads(response.content.decode('utf-8'))
id_dict['5bc893ee02743900012a339f'] = cont['id']

assert response.status_code == 201

content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
assert content == '{"id":None,"name":"prod3","price":33.35}'
