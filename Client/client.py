import socket

url = b"http://localhost:8080/hi/"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect(("localhost:8080", 80))

    s.send(url)
    resp = s.recv(4096)
    ip = s.recv(4096)

    print(resp.decode("utf-8"))
    print(ip)
