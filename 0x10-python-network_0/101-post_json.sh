#!/bin/bash
# Send a JSON via POST request using cURL
curl -s -X POST -H "Content-type: application/json" -d @"$2" "$1"
