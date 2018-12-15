import requests
import json
import time
import re
import sys
from bson.json_util import loads 
import os.path

headers = { 'Accept': 'application/json' }
data = {}
print('sending put request to http://172.18.0.11:8761/eureka/apps/ACCOUNT-SERVICE/a56f903b03f1')
response = requests.put('http://172.18.0.11:8761/eureka/apps/ACCOUNT-SERVICE/a56f903b03f1', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

