headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer 9dd4df60-8d94-44d3-bb82-75d6826430cb'}

data = {}
data = json.loads('{"name":"Test","lastSeen":"2018-12-14T08:51:43.294+0000","incomes":[{"title":"Salary","amount":30000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"Rent","amount":500.0,"period":"MONTH","icon":"home"},{"title":"Utilities","amount":200.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":100.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":60.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":1000.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":10.0,"currency":"EUR","period":"MONTH","icon":"phone"}],"saving":{"amount":2000.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":"Prova di test 1.0"}')
print('sending put request to http://localhost:6000/accounts/current')
response = requests.put('http://localhost:6000/accounts/current', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 400

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '{"timestamp":"2019-01-30T17:54:19.420+0000","status":400,"error":"Bad Request","errors":[{"codes":["NotNull.account.expenses[0].currency","NotNull.account.expenses.currency","NotNull.expenses[0].currency","NotNull.expenses.currency","NotNull.currency","NotNull.com.piggymetrics.account.domain.Currency","NotNull"],"arguments":[{"codes":["account.expenses[0].currency","expenses[0].currency"],"arguments":null,"defaultMessage":"expenses[0].currency","code":"expenses[0].currency"}],"defaultMessage":"must not be null","objectName":"account","field":"expenses[0].currency","rejectedValue":null,"bindingFailure":false,"code":"NotNull"}],"message":"Validation failed for object=\'account\'. Error count: 1","path":"/accounts/current"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

