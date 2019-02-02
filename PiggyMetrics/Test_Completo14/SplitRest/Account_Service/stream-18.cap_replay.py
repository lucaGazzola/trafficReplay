headers={'Content-type': 'application/json', 'Accept': 'application/json'}

print('sending post request to http://localhost:6000/accounts/')
json_content = {"username":"Te","password":"password"}
response = requests.post('http://localhost:6000/accounts/', data=json.dumps(json_content), headers=headers)
print('response: {0}'.format(response.content))
if response.status_code == 201:
	print('created')

assert response.status_code == 400

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '{"timestamp":"2019-01-30T17:40:56.192+0000","status":400,"error":"Bad Request","errors":[{"codes":["Length.user.username","Length.username","Length.java.lang.String","Length"],"arguments":[{"codes":["user.username","username"],"arguments":null,"defaultMessage":"username","code":"username"},20,3],"defaultMessage":"length must be between 3 and 20","objectName":"user","field":"username","rejectedValue":"Te","bindingFailure":false,"code":"Length"}],"message":"Validation failed for object=\'user\'. Error count: 1","path":"/accounts/"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

