curl -i -X POST -H 'Content-Type: application/json' http://$1:2525/imposters --data '{
	"port": 5000,
	"protocol": "http",
	"stubs": [{
		"responses": [
		{
			"is": {
				"statusCode":200,
				"headers": {"Content-Type": "application/json"},
			}
		}]
	}]
}'
