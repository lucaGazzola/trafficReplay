headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer a1527040-5fa0-4f8c-b413-e53de57cad4b'}

print('sending get request to http://localhost:7000/statistics/TestParametri')
response = requests.get('http://localhost:7000/statistics/TestParametri', headers=headers)
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

