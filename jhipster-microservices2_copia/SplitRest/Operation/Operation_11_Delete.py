import requests
import json
import time
import re
from bson.json_util import loads 
import os.path

id_dict = {}
url = 'http://localhost:8081/api/products/5bc893ee02743900012a339f/'
url = url.replace("5bc893ee02743900012a339f", id_dict['5bc893ee02743900012a339f'])
print('sending delete request to '+ url)
response = requests.delete(url, headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

