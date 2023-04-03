#!/usr/bin/bash
# Script takes a URL
# Sends a request to the URL
# and displays the size of the body of the response

url=$1
size=$(curl -s -w "%{size_download}" "$url")
echo $size
