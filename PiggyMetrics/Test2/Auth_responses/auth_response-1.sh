curl -i -X POST -H 'Content-Type: application/json' http://$1:2525/imposters --data '{
	"port": 5000,
	"protocol": "http",
	"stubs": [{
		"responses": [
		{
			"is": {
				"statusCode":200,
				"headers": {"Content-Type": "application/json"},
				"body":{"access_token":"1b4270ff-d035-4d17-a2ff-9b350dea66be","token_type":"bearer","expires_in":43199,"scope":"server"}
			}
		}]
	}]
}'
