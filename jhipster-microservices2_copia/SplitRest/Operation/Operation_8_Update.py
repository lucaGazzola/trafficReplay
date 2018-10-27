import requests
import json
import time
import re
from bson.json_util import loads 
import os.path

id_dict = {}
data = json.loads('{"id":"5bc893e202743900012a339e","name":"prod2","price":25.33}')
data['id'] = id_dict[data['id']]
print('sending put request to http://localhost:8081/api/products/')
response = requests.put('http://localhost:8081/api/products/', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
assert content == '{"id":None,"name":"prod2","price":25.33}'

