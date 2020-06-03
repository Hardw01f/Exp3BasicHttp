from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import requests
import json
import socket

address = ('127.0.0.1', 9000)


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('path = {}'.format(self.path))


        parsed_path = urlparse(self.path)
        print('parsed: path = {}, query = {}'.format(parsed_path.path, parse_qs(parsed_path.query)))

        print('headers\r\n-----\r\n{}-----'.format(self.headers))
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        if parsed_path.path == "/hi":

            self.send_response(200)
            self.send_header('Hello','BasicHTTP!')
            self.send_header('Content-Lengt', '13')
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()


            user_address = ip.encode()
            self.wfile.write(user_address)

        else:

            self.send_header('Bad','BadRequestHTTP!')
            self.end_headers()


with HTTPServer(address, MyHTTPRequestHandler) as server:
    server.serve_forever()
