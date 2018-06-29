import requests
import json
import time
import re

headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Basic YWRtaW46YWRtaW4='}

print('sending get request to http://localhost:8761/eureka/apps/delta/')
response = requests.get('http://localhost:8761/eureka/apps/delta/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
assert content == '{"applications":{"versions__delta":"3","apps__hashcode":"UP_2_","application":[]}}'

print('sending get request to http://localhost:8761/eureka/apps/delta/')
response = requests.get('http://localhost:8761/eureka/apps/delta/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
assert content == '{"applications":{"versions__delta":"3","apps__hashcode":"UP_2_","application":[]}}'

