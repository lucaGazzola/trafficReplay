curl -i -X POST -H 'Content-Type: application/json' http://$1:2525/imposters --data '{
	"port": 5000,
	"protocol": "http",
	"stubs": [{
		"responses": [
		{
			"is": {
				"statusCode":200,
				"headers": {"Content-Type": "application/json"},
				"body":{"access_token":"b52d8972-f588-4a98-86e0-65272cda65af","token_type":"bearer","expires_in":43199,"scope":"server"}
			}
		}]
	}]
}'
