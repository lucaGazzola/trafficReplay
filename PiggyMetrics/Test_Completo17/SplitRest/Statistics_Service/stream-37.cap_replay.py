headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer b5cdbce4-7c04-4b84-a31e-7e55119b9b09'}

data = {}
data = json.loads('{"name":"Test","lastSeen":"2018-12-14T08:51:43.294+0000","incomes":[{"amount":30000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"Rent","amount":500.0,"currency":"USD","period":"MONTH","icon":"home"},{"title":"Utilities","amount":200.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":100.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":60.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":1000.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":10.0,"currency":"EUR","period":"MONTH","icon":"phone"}],"saving":{"amount":2000.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":"Prova di test 1.0"}')
print('sending put request to http://localhost:7000/statistics/TestParametri')
response = requests.put('http://localhost:7000/statistics/TestParametri', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 400

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '{"timestamp":"2019-01-30T18:18:53.694+0000","status":400,"error":"Bad Request","errors":[{"codes":["NotNull.account.incomes[0].title","NotNull.account.incomes.title","NotNull.incomes[0].title","NotNull.incomes.title","NotNull.title","NotNull.java.lang.String","NotNull"],"arguments":[{"codes":["account.incomes[0].title","incomes[0].title"],"arguments":null,"defaultMessage":"incomes[0].title","code":"incomes[0].title"}],"defaultMessage":"must not be null","objectName":"account","field":"incomes[0].title","rejectedValue":null,"bindingFailure":false,"code":"NotNull"}],"message":"Validation failed for object=\'account\'. Error count: 1","path":"/statistics/TestParametri"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt
