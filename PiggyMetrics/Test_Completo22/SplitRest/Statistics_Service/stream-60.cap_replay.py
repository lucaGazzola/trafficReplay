headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer 36c3b00f-b5e5-4b3d-9128-eb2d8b15f299'}

data = {}
data = json.loads('{"name":"TestLimite2","lastSeen":"2019-02-03T10:51:59.152+0000","incomes":[{"title":"SalaryWithTwentyChar","amount":30000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"Rent","amount":500.0,"currency":"USD","period":"MONTH","icon":"home"},{"title":"Utilities","amount":200.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":100.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":60.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":1000.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":10.0,"currency":"EUR","period":"MONTH","icon":"phone"}],"saving":{"amount":2000.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":"Prova di test 1.0"}')
print('sending put request to http://localhost:7000/statistics/TestLimite2')
response = requests.put('http://localhost:7000/statistics/TestLimite2', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

