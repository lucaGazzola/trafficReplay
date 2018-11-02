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
id_dict['5bd757e4027439000182989f'] = cont['id']

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
json_content = {"name":"prod5","price":23.33}
response = requests.post('http://localhost:8081/api/products/', data=json.dumps(json_content), headers=headers)
print('response: {0}'.format(response.content))
if response.status_code == 201:
	print('created')

cont = loads(response.content.decode('utf-8'))
id_dict['5bd757f502743900018298a0'] = cont['id']

assert response.status_code == 201

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod5","price":23.33}'
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
packet_data = '[{"id":null,"name":"prod1","price":12.33},{"id":null,"name":"prod5","price":23.33}]'
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
packet_data = '[{"id":null,"name":"prod1","price":12.33},{"id":null,"name":"prod5","price":23.33}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending get request to http://localhost:8081/api/_search/products/')
response = requests.get('http://localhost:8081/api/_search/products/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 404

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"timestamp":"2018-10-29T18:57:01.665+0000","status":404,"error":"Not Found","message":"Not Found","path":"/api/_search/products"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending get request to http://localhost:8081/api/_search/products/')
response = requests.get('http://localhost:8081/api/_search/products/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 404

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"timestamp":"2018-10-29T18:57:04.064+0000","status":404,"error":"Not Found","message":"Not Found","path":"/api/_search/products"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending get request to http://localhost:8081/api/_search/products/')
response = requests.get('http://localhost:8081/api/_search/products/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 404

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"timestamp":"2018-10-29T18:57:07.870+0000","status":404,"error":"Not Found","message":"Not Found","path":"/api/_search/products"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending get request to http://localhost:8081/api/_search/products/')
response = requests.get('http://localhost:8081/api/_search/products/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 404

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"timestamp":"2018-10-29T18:57:09.319+0000","status":404,"error":"Not Found","message":"Not Found","path":"/api/_search/products"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending get request to http://localhost:8081/api/_search/products/')
response = requests.get('http://localhost:8081/api/_search/products/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 404

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"timestamp":"2018-10-29T18:57:17.560+0000","status":404,"error":"Not Found","message":"Not Found","path":"/api/_search/products"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending get request to http://localhost:8081/api/_search/products/')
response = requests.get('http://localhost:8081/api/_search/products/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 404

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"timestamp":"2018-10-29T18:57:19.493+0000","status":404,"error":"Not Found","message":"Not Found","path":"/api/_search/products"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

url = 'http://localhost:8081/api/products/5bd757f502743900018298a0/'
if '5bd757f502743900018298a0' in id_dict:	url = url.replace("5bd757f502743900018298a0", id_dict['5bd757f502743900018298a0'])
print('sending get request to '+ url)
response = requests.get(url, headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"id":null,"name":"prod5","price":23.33}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

print('sending get request to http://localhost:8081/api/_search/products/')
response = requests.get('http://localhost:8081/api/_search/products/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 404

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"timestamp":"2018-10-29T18:57:27.800+0000","status":404,"error":"Not Found","message":"Not Found","path":"/api/_search/products"}'
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
packet_data = '[{"id":null,"name":"prod1","price":12.33},{"id":null,"name":"prod5","price":23.33}]'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

