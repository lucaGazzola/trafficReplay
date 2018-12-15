import requests
import json
import time
import re
import sys
from bson.json_util import loads 
import os.path

headers = { 'Accept': 'application/json' }
headers = { 'Accept': 'application/json', 'Authorization': 'Basic YnJvd3Nlcjo=' }
passw = input('Inserisci password per davedere:')
data = {'scope': 'ui', 'grant_type': 'password', 'username': 'davedere','password': passw}
token_user = requests.post('http://172.18.0.11:5000/uaa/oauth/token', headers=headers, data=data)
token = "Bearer"+str(token_user)
headers=('Accept': 'application/json', 'Authorization': token  )

print('sending get request to http://172.18.0.11:5000/uaa/users/current')
response = requests.get('http://172.18.0.11:5000/uaa/users/current', headers=headers)
print('response: {0}'.format(response.content))

