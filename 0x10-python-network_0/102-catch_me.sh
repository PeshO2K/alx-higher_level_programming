#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me.
curl -sLX PUT 0.0.0.0:5000/catch_me_2 -d "user_id=98" -H "Origin: School"
