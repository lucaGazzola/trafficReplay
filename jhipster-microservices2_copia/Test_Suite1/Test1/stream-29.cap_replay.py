import requests
import json
import time
import re
from bson.json_util import loads 
import os.path

id_dict = {}
headers={'Content-type': 'application/json', 'Accept': 'application/json'}

if os.path.exists('Token.txt'):
	file = open('Token.txt','r')
	token = file.read()
	headers = {'Content-type': 'application/json', 'Accept': 'application/json','Authorization': 'Bearer ' + token}
	file.close()

else:
	print('sending post request to http://localhost:8080/api/authenticate')
	json_content = {"username": "admin", "password": "admin"}
	response = requests.post('http://localhost:8080/api/authenticate', data=json.dumps(json_content), headers=headers)
	content = re.sub(r'"id".*?(?=,)', '"id":None', response.content.decode('utf-8'))
	data = loads(content)
	headers = {'Content-type': 'application/json', 'Accept': 'application/json','Authorization': 'Bearer ' + data['id_token']}

print('sending get request to http://localhost:8081/api/products/')
response = requests.get('http://localhost:8081/api/products/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '[]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending post request to http://localhost:8081/api/products/')
json_content = {"name":"prod1","price":12.33}
response = requests.post('http://localhost:8081/api/products/', data=json.dumps(json_content), headers=headers)
print('response: {0}'.format(response.content))
if response.status_code == 201:
	print('created')

cont = loads(response.content.decode('utf-8'))
id_dict['5bc893d702743900012a339d'] = cont['id']

assert response.status_code == 201

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod1","price":12.33}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending get request to http://localhost:8081/api/products/')
response = requests.get('http://localhost:8081/api/products/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '[{"id":null,"name":"prod1","price":12.33}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending post request to http://localhost:8081/api/products/')
json_content = {"name":"prod2","price":23.33}
response = requests.post('http://localhost:8081/api/products/', data=json.dumps(json_content), headers=headers)
print('response: {0}'.format(response.content))
if response.status_code == 201:
	print('created')

cont = loads(response.content.decode('utf-8'))
id_dict['5bc893e202743900012a339e'] = cont['id']

assert response.status_code == 201

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod2","price":23.33}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending get request to http://localhost:8081/api/products/')
response = requests.get('http://localhost:8081/api/products/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '[{"id":null,"name":"prod1","price":12.33},{"id":null,"name":"prod2","price":23.33}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending post request to http://localhost:8081/api/products/')
json_content = {"name":"prod3","price":33.35}
response = requests.post('http://localhost:8081/api/products/', data=json.dumps(json_content), headers=headers)
print('response: {0}'.format(response.content))
if response.status_code == 201:
	print('created')

cont = loads(response.content.decode('utf-8'))
id_dict['5bc893ee02743900012a339f'] = cont['id']

assert response.status_code == 201

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod3","price":33.35}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending get request to http://localhost:8081/api/products/')
response = requests.get('http://localhost:8081/api/products/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '[{"id":null,"name":"prod1","price":12.33},{"id":null,"name":"prod2","price":23.33},{"id":null,"name":"prod3","price":33.35}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

url = 'http://localhost:8081/api/products/5bc893e202743900012a339e/'
if '5bc893e202743900012a339e' in id_dict:	url = url.replace("5bc893e202743900012a339e", id_dict['5bc893e202743900012a339e'])
print('sending get request to '+ url)
response = requests.get(url, headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod2","price":23.33}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

data = json.loads('{"id":"5bc893e202743900012a339e","name":"prod2","price":25.33}')
if data['id'] in id_dict:	data['id'] = id_dict[data['id']]
print('sending put request to http://localhost:8081/api/products/')
response = requests.put('http://localhost:8081/api/products/', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod2","price":25.33}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending get request to http://localhost:8081/api/products/')
response = requests.get('http://localhost:8081/api/products/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '[{"id":null,"name":"prod1","price":12.33},{"id":null,"name":"prod2","price":25.33},{"id":null,"name":"prod3","price":33.35}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

url = 'http://localhost:8081/api/products/5bc893ee02743900012a339f/'
if '5bc893ee02743900012a339f' in id_dict:	url = url.replace("5bc893ee02743900012a339f", id_dict['5bc893ee02743900012a339f'])
print('sending get request to '+ url)
response = requests.get(url, headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod3","price":33.35}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

url = 'http://localhost:8081/api/products/5bc893ee02743900012a339f/'
if '5bc893ee02743900012a339f' in id_dict:	url = url.replace("5bc893ee02743900012a339f", id_dict['5bc893ee02743900012a339f'])
print('sending delete request to '+ url)
response = requests.delete(url, headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

print('sending get request to http://localhost:8081/api/products/')
response = requests.get('http://localhost:8081/api/products/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '[{"id":null,"name":"prod1","price":12.33},{"id":null,"name":"prod2","price":25.33}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

