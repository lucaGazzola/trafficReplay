headers={'Content-type': 'application/json', 'Accept': 'application/json'}

print('sending post request to http://localhost:6000/accounts/')
json_content = {"username":"TestDue","password":"password"}
response = requests.post('http://localhost:6000/accounts/', data=json.dumps(json_content), headers=headers)
print('response: {0}'.format(response.content))
if response.status_code == 201:
	print('created')

