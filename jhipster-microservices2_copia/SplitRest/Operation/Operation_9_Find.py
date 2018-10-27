import requests
import json
import time
import re
from bson.json_util import loads 
import os.path

id_dict = {}
print('sending get request to http://localhost:8081/api/products/')
response = requests.get('http://localhost:8081/api/products/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
assert content == '[{"id":None,"name":"prod1","price":12.33},{"id":None,"name":"prod2","price":25.33},{"id":None,"name":"prod3","price":33.35}]'

