headers={'Content-type': 'application/json', 'Accept': 'application/json'}

print('sending post request to http://localhost:6000/accounts/')
json_content = {"username":"Test2","password":"password"}
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
packet_data = '{"name":"Test2","lastSeen":"2019-01-21T09:13:16.957+0000","incomes":null,"expenses":null,"saving":{"amount":0,"currency":"USD","interest":0,"deposit":false,"capitalization":false},"note":null}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

