headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer 3fab3679-7083-41a3-8061-765a6e648561'}

print('sending get request to http://localhost:6000/accounts/Test5')
response = requests.get('http://localhost:6000/accounts/Test5', headers=headers)
print('response: {0}'.format(response.content))

