#!/bin/bash
# Bash script displays all available HTTP methods for server using `curl`
curl -sX OPTIONS $1
