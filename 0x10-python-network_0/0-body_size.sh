#!/bin/bash
# Fetch headers only and print Content-Length
curl --head -s $1 |  grep -i "Content-Length" | awk '{print $2}'
