import requests
import json
import time
import re

req_data = {'ordered': False, 'update': 'product', 'updates': [{'q': {'_id': {'$oid': '5b73217e0274390001fce772'}}, 'u': {'_class': 'org.jhipster.store.domain.Product', '_id': {'$oid': '5b73217e0274390001fce772'}, 'name': 'prod2', 'price': '25.33'}, 'upsert': True}]}
print('assert: number of request data')
assert len(req_data)  == 3

up = 'product'
print('assert: update elements')
assert up == 'product'

order = False
print('assert: ordered elements')
assert order == False

updates = [{'q': {'_id': {'$oid': '5b73217e0274390001fce772'}}, 'u': {'_class': 'org.jhipster.store.domain.Product', '_id': {'$oid': '5b73217e0274390001fce772'}, 'name': 'prod2', 'price': '25.33'}, 'upsert': True}]
updates_test = [{'q': {'_id': {'$oid': '5b73217e0274390001fce772'}}, 'u': {'_class': 'org.jhipster.store.domain.Product', '_id': {'$oid': '5b73217e0274390001fce772'}, 'name': 'prod2', 'price': '25.33'}, 'upsert': True}]
print('assert: number of updates elements')
assert len(updates) == len(updates_test)

for i in range(0, len(updates)):
	assert len(updates[i]) == len(updates_test[i])
	for key, value in updates[i].items():
		if key != 'u' and key != '_id' and key != 'q':
			assert updates[i][key] == updates_test[i][key]
		if key == 'u':
			for keys, values in updates[i][key].items():
				if keys != '_class' and keys != '_id':
					 assert updates[i][key][keys] == updates_test[i][key][keys]

rep_data = {'n': 1, 'nModified': 1, 'ok': 1.0}
print('assert: number of reply data')
assert len(rep_data) == 3

n = 1
print('assert: n elements')
assert n  == 1

ok = 1.0
print('assert: ok elements')
assert ok  == 1.0

modif = 1
print('assert: nModified elements')
assert modif  == 1

