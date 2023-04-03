#!/bin/bash
# script sends a GET request to the URL, and displays the body of the response
# curl -s -o /dev/null -w '%{http_code}' $1 | awk {'if($0==200) {getline; print}}'
# status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1") && if [ $status_code==200 ] then curl $1 fi
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1") && [[ $status_code == 200 ]] && curl -s $1
