import requests
import json
import time
import re
import sys
from bson.json_util import loads
import os.path


headers={'Content-type': 'application/json', 'Accept': 'application/json'}

print('sending get request to http://localhost:6000/accounts/demo')
response = requests.get('http://localhost:6000/accounts/demo', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"name":"demo","lastSeen":"2019-01-21T08:30:10.141+0000","incomes":[{"title":"Salary","amount":42000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"Rent","amount":1300.0,"currency":"USD","period":"MONTH","icon":"home"},{"title":"Utilities","amount":120.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":20.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":240.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":3500.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":30.0,"currency":"EUR","period":"MONTH","icon":"phone"},{"title":"Gym","amount":700.0,"currency":"USD","period":"YEAR","icon":"sport"}],"saving":{"amount":5900.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":"demo note"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

headers={'Content-type': 'application/json', 'Accept': 'application/json'}

print('sending post request to http://localhost:6000/accounts/')
json_content = {"username":"Test","password":"password"}
response = requests.post('http://localhost:6000/accounts/', data=json.dumps(json_content), headers=headers)
print('response: {0}'.format(response.content))
if response.status_code == 201:
	print('created')

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"name":"Test","lastSeen":"2019-01-21T09:03:58.510+0000","incomes":null,"expenses":null,"saving":{"amount":0,"currency":"USD","interest":0,"deposit":false,"capitalization":false},"note":null}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer 3b52d373-6880-4c37-8623-cb152ec6ad38'}

data = {}
data = json.loads('{"name":"Test","lastSeen":"2018-12-14T08:51:43.294+0000","incomes":[{"title":"Salary","amount":30000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"Rent","amount":500.0,"currency":"USD","period":"MONTH","icon":"home"},{"title":"Utilities","amount":200.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":100.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":60.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":1000.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":10.0,"currency":"EUR","period":"MONTH","icon":"phone"}],"saving":{"amount":2000.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":"Prova di test 1.0"}')
print('sending put request to http://localhost:6000/accounts/current')
response = requests.put('http://localhost:6000/accounts/current', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

