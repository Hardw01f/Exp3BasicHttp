import socket

url = b"http://54.92.28.20/hi/"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect(("54.92.28.20", 80))

    s.send(url)
    resp = s.recv(4096)
    ip = s.recv(4096)

    print(resp.decode("utf-8"))
    print(ip)
