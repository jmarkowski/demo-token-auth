#!/bin/sh
curl \
    -X POST \
    -H "Content-type: application/json" \
    --data '{"username":"jan","password":"123"}' \
    http://127.0.0.1:5000/login
