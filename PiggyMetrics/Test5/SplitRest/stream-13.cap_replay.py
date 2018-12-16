import requests
import json
import time
import re
import sys
from bson.json_util import loads 
import os.path

headers = { 'Accept': 'application/json' }
print('sending post request to http://localhost:6000/accounts/')
json_content = {"username":"TestDue","password":"password"}
response = requests.post('http://localhost:6000/accounts/', data=json.dumps(json_content), headers=headers)
print('response: {0}'.format(response.content))
if response.status_code == 201:
	print('created')

