headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer 2d821c92-0303-4763-9d79-7fdbe742287a'}

print('sending get request to http://localhost:8000/notifications/recipients/current')
response = requests.get('http://localhost:8000/notifications/recipients/current', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
data_cont = loads(content)
if 'path' in data_cont and data_cont['path'].endswith('/'):
	data_cont['path'] = data_cont['path'][:-1]
packet_data = '{"accountName":"Test2","email":"l.ussi@campus.unimib.com","scheduledNotifications":{"REMIND":{"active":true,"frequency":"MONTHLY","lastNotified":"2019-01-18T15:25:48.545+0000"}}}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

