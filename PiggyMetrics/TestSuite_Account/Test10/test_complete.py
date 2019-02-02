import requests
import json
import time
import re
import sys
from bson.json_util import loads
import os.path


headers={'Content-type': 'application/json', 'Accept': 'application/json'}

print('sending post request to http://localhost:6000/accounts')
json_content = {"username":"Test","password":"password"}
response = requests.post('http://localhost:6000/accounts', data=json.dumps(json_content), headers=headers)
print('response: {0}'.format(response.content))
if response.status_code == 201:
	print('created')

response2 = requests.get('http://localhost:6000/accounts/', headers=headers)
assert response.status_code == response2.status_code

headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer a1527040-5fa0-4f8c-b413-e53de57cad4b'}

print('sending get request to http://localhost:6000/accounts/Test3')
response = requests.get('http://localhost:6000/accounts/Test3', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 403

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '{"error":"access_denied","error_description":"Access is denied"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer a1527040-5fa0-4f8c-b413-e53de57cad4b'}

print('sending get request to http://localhost:6000/accounts/curren')
response = requests.get('http://localhost:6000/accounts/curren', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 403

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '{"error":"access_denied","error_description":"Access is denied"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt
