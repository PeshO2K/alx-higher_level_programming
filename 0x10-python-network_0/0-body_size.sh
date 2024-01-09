#!/bin/bash
if [ "$#" -lt 1 ]; then
    echo "Usage: 0-body_size.sh URL"
    exit 1
fi
url=$1
curl --head -s $url |  grep -i "Content-Length" | awk '{print $2}'
exit