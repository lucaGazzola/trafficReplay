import requests
import json
import time
import re
import sys
from bson.json_util import loads
import os.path


headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer 2d821c92-0303-4763-9d79-7fdbe742289a'}

print('sending get request to http://localhost:8000/notifications/recipients/current')
response = requests.get('http://localhost:8000/notifications/recipients/current', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 401

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"error":"invalid_token","error_description":"2d821c92-0303-4763-9d79-7fdbe742289a"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

