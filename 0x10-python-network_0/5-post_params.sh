#!/bin/bash
# Send post request and display body of response
curl -sd "email: test@gmail.com&subject: I will always be here for PLD" -X POST $1
