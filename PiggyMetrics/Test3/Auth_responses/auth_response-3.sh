curl -i -X POST -H 'Content-Type: application/json' http://$1:2525/imposters --data '{
	"port": 5000,
	"protocol": "http",
	"stubs": [{
		"responses": [
		{
			"is": {
				"statusCode":200,
				"headers": {"Content-Type": "application/json"},
				"body":{"authorities":[],"details":{"remoteAddress":"172.18.0.11","sessionId":null,"tokenValue":"2238a999-c67a-464b-a14f-01c1329df608","tokenType":"Bearer","decodedDetails":null},"authenticated":true,"userAuthentication":{"authorities":[],"details":{"grant_type":"password","scope":"ui","username":"Test"},"authenticated":true,"principal":{"username":"Test","password":"$2a$10$xfrhM2To.iWiRdLH20h2TeYP7Sdr/9t/pKT0Bssbt6XOc9AdqyGDa","enabled":true,"authorities":null,"accountNonExpired":true,"accountNonLocked":true,"credentialsNonExpired":true},"credentials":null,"name":"Test"},"credentials":"","oauth2Request":{"clientId":"browser","scope":["ui"],"requestParameters":{"grant_type":"password","scope":"ui","username":"Test"},"resourceIds":[],"authorities":[],"approved":true,"refresh":false,"redirectUri":null,"responseTypes":[],"extensions":{},"grantType":"password","refreshTokenRequest":null},"principal":{"username":"Test","password":"$2a$10$xfrhM2To.iWiRdLH20h2TeYP7Sdr/9t/pKT0Bssbt6XOc9AdqyGDa","enabled":true,"authorities":null,"accountNonExpired":true,"accountNonLocked":true,"credentialsNonExpired":true},"clientOnly":false,"name":"Test"}
			}
		}]
	}]
}'
