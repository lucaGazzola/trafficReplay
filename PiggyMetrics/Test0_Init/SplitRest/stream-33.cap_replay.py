import requests
import json
import time
import re
import sys
from bson.json_util import loads 
import os.path

headers = { 'Accept': 'application/json' }
data = {}
print('sending put request to http://172.18.0.15:8761/eureka/apps/ACCOUNT-SERVICE/e1fe0dc0913c')
response = requests.put('http://172.18.0.15:8761/eureka/apps/ACCOUNT-SERVICE/e1fe0dc0913c', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

