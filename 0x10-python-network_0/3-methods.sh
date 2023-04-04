#!/bin/bash
# Bash script displays all available HTTP methods for server using `curl`
curl -s -X OPTIONS -I $1
