# Python Network 0: HTTP
## Task 1
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
### Curl
Flags: `-I, --head`, `-s, --silent`
```curl -I -s $URL```
```HTTP/1.1 200 OK
Server: Werkzeug/2.1.0 Python/3.8.10
Date: Tue, 09 Jan 2024 14:53:56 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 10```

