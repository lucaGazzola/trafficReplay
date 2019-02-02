headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer 2d821c92-0303-4763-9d79-7fdbe742289a'}

print('sending get request to http://localhost:8000/notifications/recipients/current')
response = requests.get('http://localhost:8000/notifications/recipients/current', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 401

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '{"error":"invalid_token","error_description":"2d821c92-0303-4763-9d79-7fdbe742289a"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

