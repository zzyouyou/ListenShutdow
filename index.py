# server.py

import http.server
import socketserver
import os


# 监听的端口号
PORT = 12345

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/shutdown':
            print(f'{PORT}: 收到关机信号，正在关机...')
            os.system('shutdown /s /t 0')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')

# 创建 HTTP 服务器并监听指定端口
with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f'服务器正在监听端口 {PORT}')
    httpd.serve_forever()
