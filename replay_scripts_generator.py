import requests
import json
import time
import re

headers={'Content-type': 'application/json', 'Authorization': 'Basic YWRtaW46YWRtaW4=', 'Accept': 'application/json'}

print('sending get request to http://localhost:8761/eureka/apps/delta HTTP/1.1\r')
response = requests.get('http://localhost:8761/eureka/apps/delta HTTP/1.1\r', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":None',str(response.content))
assert content[2:-1] == '{"applications":{"versions__delta":"4","apps__hashcode":"UP_2_","application":[]}}'

print('sending get request to http://localhost:8761/eureka/apps/CARAPP/carApp:31fb44cf7d8dd92cb1b1fee88a50dc8b/')
response = requests.get('http://localhost:8761/eureka/apps/CARAPP/carApp:31fb44cf7d8dd92cb1b1fee88a50dc8b/', headers=headers, auth=HTTPBasicAuth('admin', 'admin'))
print('response: {0}'.format(response.content))

assert response.status_code == 200

print('sending get request to http://localhost:8761/eureka/apps/CARAPP/carApp:31fb44cf7d8dd92cb1b1fee88a50dc8b/')
response = requests.get('http://localhost:8761/eureka/apps/CARAPP/carApp:31fb44cf7d8dd92cb1b1fee88a50dc8b/', headers=headers, auth=HTTPBasicAuth('admin', 'admin'))
print('response: {0}'.format(response.content))

assert response.status_code == 200

