import socket
import datetime

dt = datetime.datetime.now()

host = socket.gethostname()
ip = socket.gethostbyname(host)
print(ip)
url = b"http://localhost:8080/hi/"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, 80))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                print(data)

                if data == url:
                    print('data : {}, addr: {}'.format(data, addr))
                    #conn.sendall(b'Received: ' + data)
                    conn.send(bytes("HTTP/1.1 200 OK\n" + "Hello: BasicHTTP!\n"
                    + "Date: Tue, 26 May 2020 06:53:14 GMT\n"
                    + "Content-Length: 13\n" + "Content-Type: text/plain;", "utf-8\n" + "\n"))

                    conn.send(bytes(ip,"utf-8"))
                    break