from http.server import HTTPServer
from simple_handler import SimpleHandler

HOST, PORT = "127.0.0.1", 8000


class Server:
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.httpd = HTTPServer((self.host, self.port), SimpleHandler)

    def start(self):
        print(f"Server running at http://{self.host}:{self.port}")
        self.httpd.serve_forever()

    def stop(self):
        self.httpd.server_close()
