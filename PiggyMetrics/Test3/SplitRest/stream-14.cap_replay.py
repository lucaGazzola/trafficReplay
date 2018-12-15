import requests
import json
import time
import re
import sys
from bson.json_util import loads 
import os.path

headers = { 'Accept': 'application/json' }
data = {'grant_type': 'client_credentials'}
token_appl = requests.post('http://172.18.0.11:5000/uaa/oauth/token', headers=headers, data=data, auth=('account-service', 'acc_serv'))
token = "Bearer"+str(token_appl)
headers=('Accept': 'application/json', 'Authorization': token  )

print('sending get request to http://172.18.0.11:8761/eureka/apps/delta')
response = requests.get('http://172.18.0.11:8761/eureka/apps/delta', headers=headers)
print('response: {0}'.format(response.content))

data = {}
print('sending put request to http://172.18.0.11:8761/eureka/apps/ACCOUNT-SERVICE/a56f903b03f1')
response = requests.put('http://172.18.0.11:8761/eureka/apps/ACCOUNT-SERVICE/a56f903b03f1', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

data = {}
print('sending put request to http://172.18.0.11:8761/eureka/apps/ACCOUNT-SERVICE/a56f903b03f1')
response = requests.put('http://172.18.0.11:8761/eureka/apps/ACCOUNT-SERVICE/a56f903b03f1', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

data = {'grant_type': 'client_credentials'}
token_appl = requests.post('http://172.18.0.11:5000/uaa/oauth/token', headers=headers, data=data, auth=('account-service', 'acc_serv'))
token = "Bearer"+str(token_appl)
headers=('Accept': 'application/json', 'Authorization': token  )

print('sending get request to http://172.18.0.11:8761/eureka/apps/delta')
response = requests.get('http://172.18.0.11:8761/eureka/apps/delta', headers=headers)
print('response: {0}'.format(response.content))

data = {}
print('sending put request to http://172.18.0.11:8761/eureka/apps/ACCOUNT-SERVICE/a56f903b03f1')
response = requests.put('http://172.18.0.11:8761/eureka/apps/ACCOUNT-SERVICE/a56f903b03f1', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

data = {'grant_type': 'client_credentials'}
token_appl = requests.post('http://172.18.0.11:5000/uaa/oauth/token', headers=headers, data=data, auth=('account-service', 'acc_serv'))
token = "Bearer"+str(token_appl)
headers=('Accept': 'application/json', 'Authorization': token  )

print('sending get request to http://172.18.0.11:8761/eureka/apps/delta')
response = requests.get('http://172.18.0.11:8761/eureka/apps/delta', headers=headers)
print('response: {0}'.format(response.content))

data = {}
print('sending put request to http://172.18.0.11:8761/eureka/apps/ACCOUNT-SERVICE/a56f903b03f1')
response = requests.put('http://172.18.0.11:8761/eureka/apps/ACCOUNT-SERVICE/a56f903b03f1', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

data = {'grant_type': 'client_credentials'}
token_appl = requests.post('http://172.18.0.11:5000/uaa/oauth/token', headers=headers, data=data, auth=('account-service', 'acc_serv'))
token = "Bearer"+str(token_appl)
headers=('Accept': 'application/json', 'Authorization': token  )

print('sending get request to http://172.18.0.11:8761/eureka/apps/delta')
response = requests.get('http://172.18.0.11:8761/eureka/apps/delta', headers=headers)
print('response: {0}'.format(response.content))

data = {}
print('sending put request to http://172.18.0.11:8761/eureka/apps/ACCOUNT-SERVICE/a56f903b03f1')
response = requests.put('http://172.18.0.11:8761/eureka/apps/ACCOUNT-SERVICE/a56f903b03f1', data = json.dumps(data), headers=headers)
print('response: {0}'.format(response.content))

data = {'grant_type': 'client_credentials'}
token_appl = requests.post('http://172.18.0.11:5000/uaa/oauth/token', headers=headers, data=data, auth=('account-service', 'acc_serv'))
token = "Bearer"+str(token_appl)
headers=('Accept': 'application/json', 'Authorization': token  )

print('sending get request to http://172.18.0.11:8761/eureka/apps/delta')
response = requests.get('http://172.18.0.11:8761/eureka/apps/delta', headers=headers)
print('response: {0}'.format(response.content))

