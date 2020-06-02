# Please show HTTP Request and Response using curl command

```python:curl_result

ganbaruzoi% curl -v '13.230.219.38/hi'
*   Trying 13.230.219.38...
* TCP_NODELAY set
* Connected to 13.230.219.38 (13.230.219.38) port 80 (#0)
> GET /hi HTTP/1.1
> Host: 13.230.219.38
> User-Agent: curl/7.54.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: nginx/1.18.0
< Date: Tue, 02 Jun 2020 21:20:01 GMT
< Content-Type: text/plain; charset=utf-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< Hello: BasicHTTP!
< Content-Lengt: 13
< 
* Connection #0 to host 13.230.219.38 left intact
10.10.60.19%  

```           