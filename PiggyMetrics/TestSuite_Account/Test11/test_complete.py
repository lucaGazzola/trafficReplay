import requests
import json
import time
import re
import sys
from bson.json_util import loads
import os.path


headers={'Content-type': 'application/json', 'Accept': 'application/json'}

print('sending post request to http://localhost:6000/accounts/')
json_content = {"username":"Tes","password":"password"}
response = requests.post('http://localhost:6000/accounts/', data=json.dumps(json_content), headers=headers)
print('response: {0}'.format(response.content))
if response.status_code == 201:
	print('created')

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '{"name":"Tes","lastSeen":"2019-02-03T10:47:28.398+0000","incomes":null,"expenses":null,"saving":{"amount":0,"currency":"USD","interest":0,"deposit":false,"capitalization":false},"note":null}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

headers={'Content-type': 'application/json', 'Accept': 'application/json'}

print('sending post request to http://localhost:6000/accounts/')
json_content = {"username":"Test_venti_caratteri","password":"password"}
response = requests.post('http://localhost:6000/accounts/', data=json.dumps(json_content), headers=headers)
print('response: {0}'.format(response.content))
if response.status_code == 201:
	print('created')

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '{"name":"Test_venti_caratteri","lastSeen":"2019-02-03T10:47:39.295+0000","incomes":null,"expenses":null,"saving":{"amount":0,"currency":"USD","interest":0,"deposit":false,"capitalization":false},"note":null}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

headers={'Content-type': 'application/json', 'Accept': 'application/json'}

print('sending post request to http://localhost:6000/accounts/')
json_content = {"username":"TestLimite1","password":"pass6c"}
response = requests.post('http://localhost:6000/accounts/', data=json.dumps(json_content), headers=headers)
print('response: {0}'.format(response.content))
if response.status_code == 201:
	print('created')

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '{"name":"TestLimite1","lastSeen":"2019-02-03T10:47:50.031+0000","incomes":null,"expenses":null,"saving":{"amount":0,"currency":"USD","interest":0,"deposit":false,"capitalization":false},"note":null}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

headers={'Content-type': 'application/json', 'Accept': 'application/json'}

print('sending post request to http://localhost:6000/accounts/')
json_content = {"username":"TestLimite2","password":"password_con_quaranta_caratteri_per_test"}
response = requests.post('http://localhost:6000/accounts/', data=json.dumps(json_content), headers=headers)
print('response: {0}'.format(response.content))
if response.status_code == 201:
	print('created')

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":null',response.content.decode('utf-8'))
content = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null',content)
content = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null',content)
content = re.sub(r'"date".*?(?=,)', '"date":null',content)
data_cont = loads(content)
packet_data = '{"name":"TestLimite2","lastSeen":"2019-02-03T10:48:03.557+0000","incomes":null,"expenses":null,"saving":{"amount":0,"currency":"USD","interest":0,"deposit":false,"capitalization":false},"note":null}'
packet_data = re.sub(r'"timestamp".*?(?=,)', '"timestamp":null', packet_data)
packet_data = re.sub(r'"lastSeen".*?(?=,)', '"lastSeen":null', packet_data)
packet_data = re.sub(r'"date".*?(?=,)', '"date":null', packet_data)
data_pkt = loads(packet_data)
assert data_cont == data_pkt

headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer 9438bc8c-b03d-40fd-ac21-7d26abceedd5'}

data = {}
data = json.loads('{"name":"TestLimite1","lastSeen":"2018-12-14T08:51:43.294+0000","incomes":[{"title":"Salary","amount":30000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"Rent","amount":500.0,"currency":"USD","period":"MONTH","icon":"home"},{"title":"Utilities","amount":200.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":100.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":60.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":1000.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":10.0,"currency":"EUR","period":"MONTH","icon":"phone"}],"saving":{"amount":2000.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":""}')
print('sending put request to http://localhost:6000/accounts/current')
response = requests.put('http://localhost:6000/accounts/current', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer ce4bba12-4570-4345-ac6c-4fd451565645'}

data = {}
data = json.loads('{"name":"TestLimite2","lastSeen":"2018-12-14T08:51:43.294+0000","incomes":[{"title":"Salary","amount":30000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"Rent","amount":500.0,"currency":"USD","period":"MONTH","icon":"home"},{"title":"Utilities","amount":200.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":100.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":60.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":1000.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":10.0,"currency":"EUR","period":"MONTH","icon":"phone"}],"saving":{"amount":2000.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":"NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentiNoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVentimilaCaratteri_NoteConVenti"}')
print('sending put request to http://localhost:6000/accounts/current')
response = requests.put('http://localhost:6000/accounts/current', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer 9438bc8c-b03d-40fd-ac21-7d26abceedd5'}

data = {}
data = json.loads('{"name":"TestLimite1","lastSeen":"2018-12-14T08:51:43.294+0000","incomes":[{"title":"Salary","amount":30000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"R","amount":500.0,"currency":"USD","period":"MONTH","icon":"home"},{"title":"Utilities","amount":200.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":100.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":60.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":1000.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":10.0,"currency":"EUR","period":"MONTH","icon":"phone"}],"saving":{"amount":2000.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":"Prova di test 1.0"}')
print('sending put request to http://localhost:6000/accounts/current')
response = requests.put('http://localhost:6000/accounts/current', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer ce4bba12-4570-4345-ac6c-4fd451565645'}

data = {}
data = json.loads('{"name":"TestLimite1","lastSeen":"2018-12-14T08:51:43.294+0000","incomes":[{"title":"Salary","amount":30000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"Rent_WithTwentyChars","amount":500.0,"currency":"USD","period":"MONTH","icon":"home"},{"title":"Utilities","amount":200.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":100.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":60.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":1000.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":10.0,"currency":"EUR","period":"MONTH","icon":"phone"}],"saving":{"amount":2000.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":"Prova di test 1.0"}')
print('sending put request to http://localhost:6000/accounts/current')
response = requests.put('http://localhost:6000/accounts/current', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer 9438bc8c-b03d-40fd-ac21-7d26abceedd5'}

data = {}
data = json.loads('{"name":"TestLimite1","lastSeen":"2018-12-14T08:51:43.294+0000","incomes":[{"title":"S","amount":30000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"Rent","amount":500.0,"currency":"USD","period":"MONTH","icon":"home"},{"title":"Utilities","amount":200.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":100.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":60.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":1000.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":10.0,"currency":"EUR","period":"MONTH","icon":"phone"}],"saving":{"amount":2000.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":"Prova di test 1.0"}')
print('sending put request to http://localhost:6000/accounts/current')
response = requests.put('http://localhost:6000/accounts/current', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer ce4bba12-4570-4345-ac6c-4fd451565645'}

data = {}
data = json.loads('{"name":"TestLimite1","lastSeen":"2018-12-14T08:51:43.294+0000","incomes":[{"title":"SalaryWithTwentyChar","amount":30000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"Rent","amount":500.0,"currency":"USD","period":"MONTH","icon":"home"},{"title":"Utilities","amount":200.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":100.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":60.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":1000.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":10.0,"currency":"EUR","period":"MONTH","icon":"phone"}],"saving":{"amount":2000.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":"Prova di test 1.0"}')
print('sending put request to http://localhost:6000/accounts/current')
response = requests.put('http://localhost:6000/accounts/current', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

