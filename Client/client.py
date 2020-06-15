# クライアントを作成

import socket

bufsize = 4096
url = b"http://3.113.12.158/hi"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
    s.connect(("3.113.12.158", 80))
    # サーバにメッセージを送る
    s.sendall(url)
    # サーバからの文字列を取得する
    response = s.recv(bufsize)
    print(response.decode("utf-8"))
    # ip = s.recv(bufsize)
    # print(ip.decode("utf-8"))
