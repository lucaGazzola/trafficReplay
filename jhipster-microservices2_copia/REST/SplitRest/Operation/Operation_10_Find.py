import requests
import json
import time
import re
from bson.json_util import loads 
import os.path

id_dict = {}
url = 'http://localhost:8081/api/products/5bc893ee02743900012a339f/'
url = url.replace("5bc893ee02743900012a339f", id_dict['5bc893ee02743900012a339f'])
print('sending get request to '+ url)
response = requests.get(url, headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
assert content == '{"id":None,"name":"prod3","price":33.35}'

