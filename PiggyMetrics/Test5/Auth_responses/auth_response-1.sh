curl -i -X POST -H 'Content-Type: application/json' http://$1:2525/imposters --data '{
	"port": 5000,
	"protocol": "http",
	"stubs": [{
		"responses": [
		{
			"is": {
				"statusCode":200,
				"headers": {"Content-Type": "application/json"},
				"body":{"authorities":[],"details":{"remoteAddress":"172.18.0.11","sessionId":null,"tokenValue":"e3f5d1f7-f76d-4a31-81ef-fe4f24b7bfe2","tokenType":"Bearer","decodedDetails":null},"authenticated":true,"userAuthentication":{"authorities":[],"details":{"grant_type":"password","scope":"ui","username":"TestDue"},"authenticated":true,"principal":{"username":"TestDue","password":"$2a$10$Qq4pbVdNIFpsRa73OD6J0.ptmXnIjfWaZhhA8LIJTUywatmjHl7CG","enabled":true,"authorities":null,"accountNonExpired":true,"accountNonLocked":true,"credentialsNonExpired":true},"credentials":null,"name":"TestDue"},"credentials":"","oauth2Request":{"clientId":"browser","scope":["ui"],"requestParameters":{"grant_type":"password","scope":"ui","username":"TestDue"},"resourceIds":[],"authorities":[],"approved":true,"refresh":false,"redirectUri":null,"responseTypes":[],"extensions":{},"grantType":"password","refreshTokenRequest":null},"principal":{"username":"TestDue","password":"$2a$10$Qq4pbVdNIFpsRa73OD6J0.ptmXnIjfWaZhhA8LIJTUywatmjHl7CG","enabled":true,"authorities":null,"accountNonExpired":true,"accountNonLocked":true,"credentialsNonExpired":true},"clientOnly":false,"name":"TestDue"}
			}
		}]
	}]
}'
