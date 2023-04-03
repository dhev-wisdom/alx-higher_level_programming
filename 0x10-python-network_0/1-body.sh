#!/bin/bash
# script sends a GET request to the URL, and displays the body of the response
curl -s -o /dev/null -w '%{http_code}' $1 | awk '{ if ($http_code==200) print }'
