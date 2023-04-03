#!/bin/bash
# makes a GET request to a url and returns only the status code
curl -s -o /dev/null -w "%{http_code}" $1
