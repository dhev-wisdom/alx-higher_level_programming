#!/bin/bash
# Send a JSON via POST request using cURL
curl -X POST -H "Content-type: application/json" -d "@${json}" "$url" <<< IFS='/' read -r url json <<< "$1"
