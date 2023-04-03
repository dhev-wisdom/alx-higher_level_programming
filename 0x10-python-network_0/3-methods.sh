#!/bin/bash
# Bash script displays all available HTTP methods for server using `curl`
curl -s -l -X OPTIONS $1 | grep "Allow" |  tr -d '\r' | awk '{print $2}'
