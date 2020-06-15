# socket サーバを作成
import socket
import datetime
bufsize = 4096

host = socket.gethostname()
ip = socket.gethostbyname(host)
# today = datetime.datetime.now(datetime.timezone.utc)
# print(today)

# AF = IPv4 という意味
# TCP/IP の場合は、SOCK_STREAM を使う
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IPアドレスとポートを指定
    s.bind((socket.gethostname(),80))
    # 1 接続
    s.listen(1)
    # connection するまで待つ
    while True:
        print("server 起動")
        # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
        conn, addr = s.accept()
        with conn:
            url = conn.recv(bufsize)
            print(url.decode())
            if "/hi" in url.decode():
                conn.send(bytes("HTTP/1.1 200 OK\n"
                +"Hello: BasicHTTP!\n"
                +"Date: Tue, 26 May 2020 06:53:14 GMT\n"
                +"Content-Length: 1\n"
                +"Content-Type: text/html\n"+"\n{0}".format(ip), "utf-8"))
            else:
                break

            # conn.send(bytes(ip, "utf-8"))


            # while True:
                # # データを受け取る
                # url = conn.recv(1024).decode("utf-8")
                # print(url.split("/"))
                # if not url:
                #     break
                # # print('data : {}, addr: {}'.format(data, addr))
                # # クライアントにデータを返す(b -> byte でないといけない)
                # # conn.sendall(b'Received: ' + data)
                # conn.send(bytes("server ip: {0}".format(ip), "utf-8"))
