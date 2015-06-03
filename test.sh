#!/bin/sh

curl \
-u 'jsonrpc:347a020cb5ce709441aa42b2d5652fbb8b02e477104d1d9789f7b2d40df0' \
-d '{
    "jsonrpc": "2.0",
    "method": "updateUser",
    "id": 322123657,
    "params": {
        "id": 2,
	"is_admin": 1,
	"email": "test@test.com"
    }
}' \
http://localhost:8080/jsonrpc.php
