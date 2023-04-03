#!/bin/bash
# Make server respond with a message containing `You got me!`
curl -s -X GET '0.0.0.0:5000/catch_me' -w "You got me!"
