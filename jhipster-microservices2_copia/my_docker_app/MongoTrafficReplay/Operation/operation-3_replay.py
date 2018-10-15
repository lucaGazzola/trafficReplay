import requests
import json
import time
import re

req_data = {'filter': {}, 'find': 'product', 'limit': 20, 'sort': {'_id': 1}}
print('assert: number of request data')
assert len(req_data)  == 4

filt = {}
print('assert: filter elements')
assert filt  == {}

find = 'product'
print('assert: find elements')
assert find  == 'product'

limit = 20
print('assert: limit elements')
assert limit == 20

rep_data = {'cursor': {'firstBatch': [{'_class': 'org.jhipster.store.domain.Product', '_id': {'$oid': '5b7321750274390001fce771'}, 'name': 'prod1', 'price': '12.33'}, {'_class': 'org.jhipster.store.domain.Product', '_id': {'$oid': '5b73217e0274390001fce772'}, 'name': 'prod2', 'price': '23.33'}], 'id': {'$numberLong': '0'}, 'ns': 'store.product'}, 'ok': 1.0}
print('assert: number of reply data')
assert len(rep_data) == 2

cursor = {'firstBatch': [{'_class': 'org.jhipster.store.domain.Product', '_id': {'$oid': '5b7321750274390001fce771'}, 'name': 'prod1', 'price': '12.33'}, {'_class': 'org.jhipster.store.domain.Product', '_id': {'$oid': '5b73217e0274390001fce772'}, 'name': 'prod2', 'price': '23.33'}], 'id': {'$numberLong': '0'}, 'ns': 'store.product'}
cursor_test = {'firstBatch': [{'_class': 'org.jhipster.store.domain.Product', '_id': {'$oid': '5b7321750274390001fce771'}, 'name': 'prod1', 'price': '12.33'}, {'_class': 'org.jhipster.store.domain.Product', '_id': {'$oid': '5b73217e0274390001fce772'}, 'name': 'prod2', 'price': '23.33'}], 'id': {'$numberLong': '0'}, 'ns': 'store.product'}
print('assert: number of cursor data')
assert len(cursor) == len(cursor_test) 

for key, value in cursor.items():
	if key == 'firstBatch':
		assert len(cursor[key])  == len(cursor_test[key]) 
		for i in range(0, len(cursor[key])):
			for keys, values in cursor[key][i].items():
				if keys != '_class' and keys != '_id':
					assert cursor[key][i][keys] ==  cursor_test[key][i][keys] 
