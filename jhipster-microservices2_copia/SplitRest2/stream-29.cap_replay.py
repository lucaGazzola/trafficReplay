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
	print(token)
	headers = {'Content-type': 'application/json', 'Accept': 'application/json','Authorization': 'Bearer ' + token}

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
print(str(json_content))
response = requests.post('http://localhost:8081/api/products/', data=json.dumps(json_content), headers=headers)
if response.status_code == 201:
	print('created')

cont = loads(response.content.decode('utf-8'))
id_dict['5bd5f70b0e8e3d0001891c24'] = cont['id']

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

url = 'http://localhost:8081/api/products/5bd5f70b0e8e3d0001891c24/'
if '5bd5f70b0e8e3d0001891c24' in id_dict:	url = url.replace("5bd5f70b0e8e3d0001891c24", id_dict['5bd5f70b0e8e3d0001891c24'])
print('sending get request to '+ url)
response = requests.get(url, headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod1","price":12.33}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

data = json.loads('{"id":"5bd5f70b0e8e3d0001891c24","name":"prod1","price":15.33}')
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
packet_data = '{"id":null,"name":"prod1","price":15.33}'
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
packet_data = '[{"id":null,"name":"prod1","price":15.33}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending post request to http://localhost:8081/api/products/')
json_content = {"name":"prod3","price":25.33}
print(str(json_content))
response = requests.post('http://localhost:8081/api/products/', data=json.dumps(json_content), headers=headers)
if response.status_code == 201:
	print('created')

cont = loads(response.content.decode('utf-8'))
id_dict['5bd5f71e0e8e3d0001891c25'] = cont['id']

assert response.status_code == 201

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod3","price":25.33}'
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
packet_data = '[{"id":null,"name":"prod1","price":15.33},{"id":null,"name":"prod3","price":25.33}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending post request to http://localhost:8081/api/products/')
json_content = {"name":"prod4","price":29}
print(str(json_content))
response = requests.post('http://localhost:8081/api/products/', data=json.dumps(json_content), headers=headers)
if response.status_code == 201:
	print('created')

cont = loads(response.content.decode('utf-8'))
id_dict['5bd5f72d0e8e3d0001891c26'] = cont['id']

assert response.status_code == 201

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod4","price":29}'
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
packet_data = '[{"id":null,"name":"prod1","price":15.33},{"id":null,"name":"prod3","price":25.33},{"id":null,"name":"prod4","price":29}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending post request to http://localhost:8081/api/products/')
json_content = {"name":"prod7","price":55}
print(str(json_content))
response = requests.post('http://localhost:8081/api/products/', data=json.dumps(json_content), headers=headers)
if response.status_code == 201:
	print('created')

cont = loads(response.content.decode('utf-8'))
id_dict['5bd5f7380e8e3d0001891c27'] = cont['id']

assert response.status_code == 201

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod7","price":55}'
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
packet_data = '[{"id":null,"name":"prod1","price":15.33},{"id":null,"name":"prod3","price":25.33},{"id":null,"name":"prod4","price":29},{"id":null,"name":"prod7","price":55}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending post request to http://localhost:8081/api/products/')
json_content = {"name":"prod23","price":15.77}
print(str(json_content))
response = requests.post('http://localhost:8081/api/products/', data=json.dumps(json_content), headers=headers)
if response.status_code == 201:
	print('created')

cont = loads(response.content.decode('utf-8'))
id_dict['5bd5f7460e8e3d0001891c28'] = cont['id']

assert response.status_code == 201

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod23","price":15.77}'
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
packet_data = '[{"id":null,"name":"prod1","price":15.33},{"id":null,"name":"prod3","price":25.33},{"id":null,"name":"prod4","price":29},{"id":null,"name":"prod7","price":55},{"id":null,"name":"prod23","price":15.77}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

url = 'http://localhost:8081/api/products/5bd5f71e0e8e3d0001891c25/'
if '5bd5f71e0e8e3d0001891c25' in id_dict:	url = url.replace("5bd5f71e0e8e3d0001891c25", id_dict['5bd5f71e0e8e3d0001891c25'])
print('sending get request to '+ url)
response = requests.get(url, headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod3","price":25.33}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

url = 'http://localhost:8081/api/products/5bd5f71e0e8e3d0001891c25/'
if '5bd5f71e0e8e3d0001891c25' in id_dict:	url = url.replace("5bd5f71e0e8e3d0001891c25", id_dict['5bd5f71e0e8e3d0001891c25'])
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
packet_data = '[{"id":null,"name":"prod1","price":15.33},{"id":null,"name":"prod4","price":29},{"id":null,"name":"prod7","price":55},{"id":null,"name":"prod23","price":15.77}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

url = 'http://localhost:8081/api/products/5bd5f7380e8e3d0001891c27/'
if '5bd5f7380e8e3d0001891c27' in id_dict:	url = url.replace("5bd5f7380e8e3d0001891c27", id_dict['5bd5f7380e8e3d0001891c27'])
print('sending get request to '+ url)
response = requests.get(url, headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod7","price":55}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

url = 'http://localhost:8081/api/products/5bd5f7380e8e3d0001891c27/'
if '5bd5f7380e8e3d0001891c27' in id_dict:	url = url.replace("5bd5f7380e8e3d0001891c27", id_dict['5bd5f7380e8e3d0001891c27'])
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
packet_data = '[{"id":null,"name":"prod1","price":15.33},{"id":null,"name":"prod4","price":29},{"id":null,"name":"prod23","price":15.77}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

url = 'http://localhost:8081/api/products/5bd5f7460e8e3d0001891c28/'
if '5bd5f7460e8e3d0001891c28' in id_dict:	url = url.replace("5bd5f7460e8e3d0001891c28", id_dict['5bd5f7460e8e3d0001891c28'])
print('sending get request to '+ url)
response = requests.get(url, headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod23","price":15.77}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

data = json.loads('{"id":"5bd5f7460e8e3d0001891c28","name":"prod23","price":15.5}')
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
packet_data = '{"id":null,"name":"prod23","price":15.5}'
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
packet_data = '[{"id":null,"name":"prod1","price":15.33},{"id":null,"name":"prod4","price":29},{"id":null,"name":"prod23","price":15.5}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

