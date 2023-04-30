#!/bin/bash
# A script to send a request to a URL and display size of body of the response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f 2
