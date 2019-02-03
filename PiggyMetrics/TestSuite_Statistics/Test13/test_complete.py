import requests
import json
import time
import re
import sys
from bson.json_util import loads
import os.path


headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer 5ee18008-f2f0-445f-8acd-342d4efc38cc'}

data = {}
data = json.loads('{"name":"TestLimite3","lastSeen":"2018-12-14T08:51:43.294+0000","incomes":[{"title":"Salary","amount":30000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"","amount":500.0,"currency":"USD","period":"MONTH","icon":"home"},{"title":"Utilities","amount":200.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":100.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":60.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":1000.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":10.0,"currency":"EUR","period":"MONTH","icon":"phone"}],"saving":{"amount":2000.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":"Prova di test 1.0"}')
print('sending put request to http://localhost:7000/statistics/TestLimite2')
response = requests.put('http://localhost:7000/statistics/TestLimite2', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 400

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '{"timestamp":"2019-02-03T16:32:32.603+0000","status":400,"error":"Bad Request","errors":[{"codes":["Length.account.expenses[0].title","Length.account.expenses.title","Length.expenses[0].title","Length.expenses.title","Length.title","Length.java.lang.String","Length"],"arguments":[{"codes":["account.expenses[0].title","expenses[0].title"],"arguments":null,"defaultMessage":"expenses[0].title","code":"expenses[0].title"},20,1],"defaultMessage":"length must be between 1 and 20","objectName":"account","field":"expenses[0].title","rejectedValue":"","bindingFailure":false,"code":"Length"}],"message":"Validation failed for object=\'account\'. Error count: 1","path":"/statistics/TestLimite2"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer 5ee18008-f2f0-445f-8acd-342d4efc38cc'}

data = {}
data = json.loads('{"name":"TestLimite3","lastSeen":"2018-12-14T08:51:43.294+0000","incomes":[{"title":"Salary","amount":30000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"Rent_WithTwentyChars1","amount":500.0,"currency":"USD","period":"MONTH","icon":"home"},{"title":"Utilities","amount":200.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":100.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":60.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":1000.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":10.0,"currency":"EUR","period":"MONTH","icon":"phone"}],"saving":{"amount":2000.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":"Prova di test 1.0"}')
print('sending put request to http://localhost:7000/statistics/TestLimite2')
response = requests.put('http://localhost:7000/statistics/TestLimite2', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 400

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '{"timestamp":"2019-02-03T16:32:49.249+0000","status":400,"error":"Bad Request","errors":[{"codes":["Length.account.expenses[0].title","Length.account.expenses.title","Length.expenses[0].title","Length.expenses.title","Length.title","Length.java.lang.String","Length"],"arguments":[{"codes":["account.expenses[0].title","expenses[0].title"],"arguments":null,"defaultMessage":"expenses[0].title","code":"expenses[0].title"},20,1],"defaultMessage":"length must be between 1 and 20","objectName":"account","field":"expenses[0].title","rejectedValue":"Rent_WithTwentyChars1","bindingFailure":false,"code":"Length"}],"message":"Validation failed for object=\'account\'. Error count: 1","path":"/statistics/TestLimite2"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer 5ee18008-f2f0-445f-8acd-342d4efc38cc'}

data = {}
data = json.loads('{"name":"TestLimite3","lastSeen":"2018-12-14T08:51:43.294+0000","incomes":[{"title":"","amount":30000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"Rent","amount":500.0,"currency":"USD","period":"MONTH","icon":"home"},{"title":"Utilities","amount":200.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":100.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":60.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":1000.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":10.0,"currency":"EUR","period":"MONTH","icon":"phone"}],"saving":{"amount":2000.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":"Prova di test 1.0"}')
print('sending put request to http://localhost:7000/statistics/TestLimite2')
response = requests.put('http://localhost:7000/statistics/TestLimite2', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 400

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '{"timestamp":"2019-02-03T16:33:06.923+0000","status":400,"error":"Bad Request","errors":[{"codes":["Length.account.incomes[0].title","Length.account.incomes.title","Length.incomes[0].title","Length.incomes.title","Length.title","Length.java.lang.String","Length"],"arguments":[{"codes":["account.incomes[0].title","incomes[0].title"],"arguments":null,"defaultMessage":"incomes[0].title","code":"incomes[0].title"},20,1],"defaultMessage":"length must be between 1 and 20","objectName":"account","field":"incomes[0].title","rejectedValue":"","bindingFailure":false,"code":"Length"}],"message":"Validation failed for object=\'account\'. Error count: 1","path":"/statistics/TestLimite2"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer 5ee18008-f2f0-445f-8acd-342d4efc38cc'}

data = {}
data = json.loads('{"name":"TestLimite3","lastSeen":"2018-12-14T08:51:43.294+0000","incomes":[{"title":"SalaryWithTwentyChar1","amount":30000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"Rent","amount":500.0,"currency":"USD","period":"MONTH","icon":"home"},{"title":"Utilities","amount":200.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":100.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":60.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":1000.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":10.0,"currency":"EUR","period":"MONTH","icon":"phone"}],"saving":{"amount":2000.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":"Prova di test 1.0"}')
print('sending put request to http://localhost:7000/statistics/TestLimite2')
response = requests.put('http://localhost:7000/statistics/TestLimite2', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 400

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '{"timestamp":"2019-02-03T16:33:32.502+0000","status":400,"error":"Bad Request","errors":[{"codes":["Length.account.incomes[0].title","Length.account.incomes.title","Length.incomes[0].title","Length.incomes.title","Length.title","Length.java.lang.String","Length"],"arguments":[{"codes":["account.incomes[0].title","incomes[0].title"],"arguments":null,"defaultMessage":"incomes[0].title","code":"incomes[0].title"},20,1],"defaultMessage":"length must be between 1 and 20","objectName":"account","field":"incomes[0].title","rejectedValue":"SalaryWithTwentyChar1","bindingFailure":false,"code":"Length"}],"message":"Validation failed for object=\'account\'. Error count: 1","path":"/statistics/TestLimite2"}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

