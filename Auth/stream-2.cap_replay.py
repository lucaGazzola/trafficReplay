import requests
import json
import time
import re

headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImF1dGgiOiJST0xFX0FETUlOLFJPTEVfVVNFUiIsImV4cCI6MTUzNzAxNzM2Nn0.PcN2ObELsOkxxSg42pZubPmOY1rQtpvP-dWxvW36x02VWWgeIw358PhdmDC0BKS9GBYBJB6mZM3gk6nIowQOog'}

print('sending get request to http://localhost:8080/api/account/')
response = requests.get('http://localhost:8080/api/account/', headers=headers)
print('response: {0}'.format(response.content))

assert response.status_code == 200

content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
assert content == '{"id":None,"login":"admin","firstName":"Administrator","lastName":"Administrator","email":"admin@localhost","imageUrl":"","activated":true,"langKey":"it","createdBy":"system","createdDate":"2018-08-09T11:28:13.855587Z","lastModifiedBy":"system","lastModifiedDate":null,"authorities":["ROLE_USER","ROLE_ADMIN"]}'

