headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer 9dd4df60-8d94-44d3-bb82-75d6826430cb'}

data = {}
data = json.loads('{"accountName":"TestParametri","scheduledNotifications":{"REMIND":{"active":true,"frequency":"MONTHLY","lastNotified":"2019-01-18T15:25:48.545+0000"}}}')
print('sending put request to http://localhost:8000/notifications/recipients/current')
response = requests.put('http://localhost:8000/notifications/recipients/current', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 400

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '{"timestamp":"2019-01-30T18:14:03.781+0000","status":400,"error":"Bad Request","errors":[{"codes":["NotNull.recipient.email","NotNull.email","NotNull.java.lang.String","NotNull"],"arguments":[{"codes":["recipient.email","email"],"arguments":null,"defaultMessage":"email","code":"email"}],"defaultMessage":"must not be null","objectName":"recipient","field":"email","rejectedValue":null,"bindingFailure":false,"code":"NotNull"}],"message":"Validation failed for object=\'recipient\'. Error count: 1","path":"/notifications/recipients/current"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt
