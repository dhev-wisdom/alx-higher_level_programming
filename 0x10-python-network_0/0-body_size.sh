#!/usr/bin/bash
# Script takes a URL, sends a request and displays the size of the body
echo $(curl -s -w "%{size_download}" "$1")
