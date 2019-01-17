curl -i -X POST -H 'Content-Type: application/json' http://$1:2525/imposters --data '{
	"port": 5000,
	"protocol": "http",
	"stubs": [{
		"responses": [
		{
			"is": {
				"statusCode":200,
				"headers": {"Content-Type": "application/json"},
				"body":{"authorities":[],"details":{"remoteAddress":"172.18.0.15","sessionId":null,"tokenValue":"3cbe7001-0fac-4c03-b834-edbf37b4d88c","tokenType":"Bearer","decodedDetails":null},"authenticated":true,"userAuthentication":{"authorities":[],"details":{"grant_type":"password","scope":"ui","username":"LucaTest"},"authenticated":true,"principal":{"username":"LucaTest","password":"$2a$10$MJBpsHdrcBK.j0KZYn/Fle1gHshE74G5ohkCOyeEBqU7bf0psMj4S","enabled":true,"authorities":null,"accountNonExpired":true,"accountNonLocked":true,"credentialsNonExpired":true},"credentials":null,"name":"LucaTest"},"clientOnly":false,"principal":{"username":"LucaTest","password":"$2a$10$MJBpsHdrcBK.j0KZYn/Fle1gHshE74G5ohkCOyeEBqU7bf0psMj4S","enabled":true,"authorities":null,"accountNonExpired":true,"accountNonLocked":true,"credentialsNonExpired":true},"credentials":"","oauth2Request":{"clientId":"browser","scope":["ui"],"requestParameters":{"grant_type":"password","scope":"ui","username":"LucaTest"},"resourceIds":[],"authorities":[],"approved":true,"refresh":false,"redirectUri":null,"responseTypes":[],"extensions":{},"grantType":"password","refreshTokenRequest":null},"name":"LucaTest"}
			}
		}]
	}]
}'
