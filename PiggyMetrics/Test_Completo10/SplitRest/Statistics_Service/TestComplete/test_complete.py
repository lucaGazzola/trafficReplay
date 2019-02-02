import requests
import json
import time
import re
import sys
from bson.json_util import loads
import os.path


headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer cfecb34e-43a7-4f0c-b121-ecd957e5174f'}

data = {}
data = json.loads('{"name":"Test","lastSeen":"2018-12-14T08:51:43.294+0000","incomes":[{"title":"Salary","amount":30000.0,"currency":"USD","period":"YEAR","icon":"wallet"},{"title":"Scholarship","amount":500.0,"currency":"USD","period":"MONTH","icon":"edu"}],"expenses":[{"title":"Rent","amount":500.0,"currency":"USD","period":"MONTH","icon":"home"},{"title":"Utilities","amount":200.0,"currency":"USD","period":"MONTH","icon":"utilities"},{"title":"Meal","amount":100.0,"currency":"USD","period":"DAY","icon":"meal"},{"title":"Gas","amount":60.0,"currency":"USD","period":"MONTH","icon":"gas"},{"title":"Vacation","amount":1000.0,"currency":"EUR","period":"YEAR","icon":"island"},{"title":"Phone","amount":10.0,"currency":"EUR","period":"MONTH","icon":"phone"}],"saving":{"amount":2000.0,"currency":"USD","interest":3.32,"deposit":true,"capitalization":false},"note":"Prova di test 1.0"}')
print('sending put request to http://localhost:7000/statistics/Test6')
response = requests.put('http://localhost:7000/statistics/Test6', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200
