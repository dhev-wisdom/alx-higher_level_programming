#!/usr/bin/bash
# Script takes a URL, sends a request and displays the size of the body
curl -s -o /dev/null -w %{size_download} $1
