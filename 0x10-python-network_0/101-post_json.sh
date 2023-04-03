#!/bin/bash
# Send a JSON via POST request using cURL
IFS='/' read -r url json <<< "$1" && curl -X POST -H "Content-type: application/json" -d "@${json}" "$url"
