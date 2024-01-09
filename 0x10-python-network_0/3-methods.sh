#!/bin/bash
# Fetch headers only and print allowed methods
curl --head -s $1 |  grep -i "Allow" | cut -d ' ' -f2-
