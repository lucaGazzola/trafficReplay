import requests
import json
import time
import re

req_data = {'delete': 'product', 'deletes': [{'limit': 0, 'q': {'_id': {'$oid': '5b7321830274390001fce773'}}}], 'ordered': False}
print('assert: number of request data')
assert len(req_data)  == 3

delete = 'product'
print('assert: delete elements')
assert delete == 'product'

order = False
print('assert: ordered elements')
assert order == False

deletes = [{'limit': 0, 'q': {'_id': {'$oid': '5b7321830274390001fce773'}}}]
deletes_test = [{'limit': 0, 'q': {'_id': {'$oid': '5b7321830274390001fce773'}}}]
print('assert: number of deletes elements')
assert len(deletes) == len(deletes_test) 

for i in range(0, len(deletes)):
	assert len(deletes[i]) == len(deletes_test[i])
	for key, value in deletes[i].items():
		if key == 'q':
			for keys, values in deletes[i][key].items():
				assert deletes[i][key][keys]['$oid'] == deletes_test[i][key][keys]['$oid']
		else:
			assert deletes[i][key] == deletes_test[i][key]

rep_data = {'n': 1, 'ok': 1.0}
print('assert: number of reply data')
assert len(rep_data) == 2

n = 1
print('assert: n elements')
assert n  == 1

ok = 1.0
print('assert: ok elements')
assert ok  == 1.0

