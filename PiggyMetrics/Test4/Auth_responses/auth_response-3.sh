curl -i -X POST -H 'Content-Type: application/json' http://$1:2525/imposters --data '{
	"port": 5000,
	"protocol": "http",
	"stubs": [{
		"responses": [
		{
			"is": {
				"statusCode":200,
				"headers": {"Content-Type": "application/json"},
				"body":{"authorities":[],"details":{"remoteAddress":"172.18.0.11","sessionId":null,"tokenValue":"1b4270ff-d035-4d17-a2ff-9b350dea66be","tokenType":"Bearer","decodedDetails":null},"authenticated":true,"userAuthentication":null,"credentials":"","oauth2Request":{"clientId":"account-service","scope":["server"],"requestParameters":{"grant_type":"client_credentials"},"resourceIds":[],"authorities":[],"approved":true,"refresh":false,"redirectUri":null,"responseTypes":[],"extensions":{},"grantType":"client_credentials","refreshTokenRequest":null},"principal":"account-service","clientOnly":true,"name":"account-service"}
			}
		}]
	}]
}'
