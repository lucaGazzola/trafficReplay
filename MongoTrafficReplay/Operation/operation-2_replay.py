import requests
import json
import time
import re

req_data = {'documents': [{'_class': 'org.jhipster.store.domain.Product', '_id': {'$oid': '5b73217e0274390001fce772'}, 'name': 'prod2', 'price': '23.33'}], 'insert': 'product', 'ordered': True}
print('assert: number of request data')
assert len(req_data)  == 3

doc = [{'_class': 'org.jhipster.store.domain.Product', '_id': {'$oid': '5b73217e0274390001fce772'}, 'name': 'prod2', 'price': '23.33'}]
doc_test = [{'_class': 'org.jhipster.store.domain.Product', '_id': {'$oid': '5b73217e0274390001fce772'}, 'name': 'prod2', 'price': '23.33'}]
print('assert: number of document elements')
assert len(doc) == len(doc_test)

for i in range(0, len(doc)):
	assert len(doc[i]) == len(doc_test[i])
	for key, value in doc[i].items():
		if key != '_class' and key != '_id':
			assert doc[i][key] == doc_test[i][key]

ins = 'product'
print('assert: insert elements')
assert ins  == 'product'

order = True
print('assert: order elements')
assert order  == True

rep_data = {'n': 1, 'ok': 1.0}
print('assert: number of reply data')
assert len(rep_data)  == 2

n = 1
print('assert: n elements')
assert n  == 1

ok = 1.0
print('assert: ok elements')
assert ok  == 1.0

