#!/bin/bash
# Send post request and display body of response
curl -sd "email: test@gmail.com" -d "subject: I will always be here for PLD" $1
