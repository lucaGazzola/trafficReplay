import requests
import json
import time
import re
import urllib.request
import json
from requests.auth import HTTPBasicAuth
from bson.json_util import loads


def main():

	# --------------------
	id_dict = {}
	# --------------------
	headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

	print('sending post request to http://localhost:8080/api/authenticate')
	json_content = {"username": "admin", "password": "admin"}
	print(str(json_content))
	response = requests.post('http://localhost:8080/api/authenticate', data=json.dumps(json_content), headers=headers)
	content = re.sub(r'"id".*?(?=,)', '"id":None', response.content.decode('utf-8'))
	print(content)
	data = loads(content)
	print(data['id_token'])
	headers = {'Content-type': 'application/json', 'Accept': 'application/json','Authorization': 'Bearer '+data['id_token']}
	print(headers)

	print('sending post request to http://localhost:8081/api/products/')
	json_content = {"name": "prod1", "price": 12.33}
	print(str(json_content))
	response = requests.post('http://localhost:8081/api/products/', data=json.dumps(json_content), headers=headers)
	if response.status_code == 201:
		print('created')
	else:
		print(response.content)

	real_id = '5b9a323d02743900016377ec'
	print(response.status_code)

	assert response.status_code == 201

	content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
	assert content == '{"id":None,"name":"prod1","price":12.33}'

	print('sending get request to http://localhost:8081/api/products/')
	response = requests.get('http://localhost:8081/api/products/', headers=headers)
	print('response: {0}'.format(response.content))

	assert response.status_code == 200

	content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
	assert content == '[{"id":None,"name":"prod1","price":12.33}]'

	print('sending post request to http://localhost:8081/api/products/')
	json_content = {"name":"prod2","price":23.33}
	print(str(json_content))
	response = requests.post('http://localhost:8081/api/products/', data=json.dumps(json_content), headers=headers)
	if response.status_code == 201:
		print('created')

	real_id = '5b9a324502743900016377ed'

	assert response.status_code == 201

	content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
	assert content == '{"id":None,"name":"prod2","price":23.33}'

	print('sending get request to http://localhost:8081/api/products/')
	response = requests.get('http://localhost:8081/api/products/', headers=headers)
	print('response: {0}'.format(response.content))

	assert response.status_code == 200

	content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
	assert content == '[{"id":None,"name":"prod1","price":12.33},{"id":None,"name":"prod2","price":23.33}]'

	print('sending post request to http://localhost:8081/api/products/')
	json_content = {"id":"5b9a325102743900016377ee","name":"prod3","price":33.33}
	print(str(json_content))
	response = requests.post('http://localhost:8081/api/products/', data=json.dumps(json_content), headers=headers)
	if response.status_code == 201:
		print('created')

	real_id = '5b9a325102743900016377ee'

	assert response.status_code == 201

	#-----------------------------------------
	print("contenuto della risposta")
	print(response.content)
	data = json.loads(response.content.decode('utf-8'))
	print(data['id'])
	id_dict[real_id] = str(data['id'])
	print(id_dict[real_id])
	#---------------------------------------

	content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
	assert content == '{"id":None,"name":"prod3","price":33.33}'

	print('sending get request to http://localhost:8081/api/products/')
	response = requests.get('http://localhost:8081/api/products/', headers=headers)
	print('response: {0}'.format(response.content))

	assert response.status_code == 200

	content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
	assert content == '[{"id":None,"name":"prod1","price":12.33},{"id":None,"name":"prod2","price":23.33},{"id":None,"name":"prod3","price":33.33}]'

	print('sending get request to http://localhost:8081/api/products/5b9a324502743900016377ed/')
	response = requests.get('http://localhost:8081/api/products/5b9a324502743900016377ed/', headers=headers)
	print('response: {0}'.format(response.content))

	assert response.status_code == 200

	content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
	assert content == '{"id":None,"name":"prod2","price":23.33}'

	assert response.status_code == 200

	content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
	assert content == '{"id":None,"name":"prod2","price":25.33}'

	print('sending get request to http://localhost:8081/api/products/')
	response = requests.get('http://localhost:8081/api/products/', headers=headers)
	print('response: {0}'.format(response.content))

	assert response.status_code == 200

	content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
	assert content == '[{"id":None,"name":"prod1","price":12.33},{"id":None,"name":"prod2","price":25.33},{"id":None,"name":"prod3","price":33.33}]'

	print('sending get request to http://localhost:8081/api/products/5b9a325102743900016377ee/')
	response = requests.get('http://localhost:8081/api/products/5b9a325102743900016377ee/', headers=headers)
	print('response: {0}'.format(response.content))

	assert response.status_code == 200

	content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
	assert content == '{"id":None,"name":"prod3","price":33.33}'

	print('sending get request to http://localhost:8081/api/products/')
	response = requests.get('http://localhost:8081/api/products/', headers=headers)
	print('response: {0}'.format(response.content))

	assert response.status_code == 200

	content = re.sub(r'"id".*?(?=,)', '"id":None',response.content.decode('utf-8'))
	assert content == '[{"id":None,"name":"prod1","price":12.33},{"id":None,"name":"prod2","price":25.33}]'

if __name__ == "__main__":
    main()