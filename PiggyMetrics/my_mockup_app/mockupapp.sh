curl -i -X POST -H 'Content-Type: application/json' http://172.18.0.6:2525/imposters --data '{
  "port": 5000,
  "protocol": "http",
  "mode": "binary",
  "stubs": [{
    "responses": [
      {
          "is": {
            "statusCode": 200,
            "headers": {
              "Content-Type": "application/json"
            }
          }
        }
    ]
  }]
}'
