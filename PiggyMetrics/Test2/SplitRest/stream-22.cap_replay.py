import requests
import json
import time
import re
import sys
from bson.json_util import loads 
import os.path

headers = { 'Accept': 'application/json' }
print('sending post request to http://172.18.0.11:5000/uaa/oauth/token')
json_content = grant_type=client_credentials&scope=server
response = requests.post('http://172.18.0.11:5000/uaa/oauth/token', data=json.dumps(json_content), headers=headers)
print('response: {0}'.format(response.content))
if response.status_code == 201:
	print('created')

