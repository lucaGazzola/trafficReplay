import requests
import json
import time
import re
import sys
from bson.json_util import loads 
import os.path

headers = { 'Accept': 'application/json' }
data = {'grant_type': 'client_credentials'}
token_appl = requests.post('http://172.18.0.15:5000/uaa/oauth/token', headers=headers, data=data, auth=('account-service', 'acc_serv'))
token = "Bearer"+str(token_appl)
headers=('Accept': 'application/json', 'Authorization': token  )

print('sending get request to http://172.18.0.15:8761/eureka/apps/')
response = requests.get('http://172.18.0.15:8761/eureka/apps/', headers=headers)
print('response: {0}'.format(response.content))

print('sending post request to http://172.18.0.15:8761/eureka/apps/ACCOUNT-SERVICE')
json_content = {"instance":{"instanceId":"e1fe0dc0913c:account-service:6000","hostName":"172.18.0.15","app":"ACCOUNT-SERVICE","ipAddr":"172.18.0.15","status":"UP","overriddenStatus":"UNKNOWN","port":{"$":6000,"@enabled":"true"},"securePort":{"$":443,"@enabled":"false"},"countryId":1,"dataCenterInfo":{"@class":"com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo","name":"MyOwn"},"leaseInfo":{"renewalIntervalInSecs":30,"durationInSecs":90,"registrationTimestamp":0,"lastRenewalTimestamp":0,"evictionTimestamp":0,"serviceUpTimestamp":0},"metadata":{"management.port":"6000"},"homePageUrl":"http://172.18.0.15:6000/","statusPageUrl":"http://172.18.0.15:6000/actuator/info","healthCheckUrl":"http://172.18.0.15:6000/actuator/health","vipAddress":"account-service","secureVipAddress":"account-service","isCoordinatingDiscoveryServer":"false","lastUpdatedTimestamp":"1544704046165","lastDirtyTimestamp":"1544704049896"}}
response = requests.post('http://172.18.0.15:8761/eureka/apps/ACCOUNT-SERVICE', data=json.dumps(json_content), headers=headers)
print('response: {0}'.format(response.content))
if response.status_code == 201:
	print('created')

data = {'grant_type': 'client_credentials'}
token_appl = requests.post('http://172.18.0.15:5000/uaa/oauth/token', headers=headers, data=data, auth=('account-service', 'acc_serv'))
token = "Bearer"+str(token_appl)
headers=('Accept': 'application/json', 'Authorization': token  )

print('sending get request to http://172.18.0.15:8761/eureka/apps/delta')
response = requests.get('http://172.18.0.15:8761/eureka/apps/delta', headers=headers)
print('response: {0}'.format(response.content))

