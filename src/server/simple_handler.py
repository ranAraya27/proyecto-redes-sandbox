import os
import json
from http.server import BaseHTTPRequestHandler

from web_page.index import create_main_page
from inventory.products import PRODUCTS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(BASE_DIR, "web_page")


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html" or self.path == "/home":
            try:
                main_page = create_main_page()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(main_page.encode("utf-8"))
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Error loading main page")

        elif self.path == "/web_page/style.css":
            try:
                file_path = os.path.join(WEB_DIR, "style.css")
                with open(file_path, "rb") as f:
                    body = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/css; charset=utf-8")
                self.end_headers()
                self.wfile.write(body)
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Error loading CSS")

        elif self.path == "/api/products":
            body = json.dumps(PRODUCTS).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(body)

        else:
            self.send_response(404)
            self.end_headers()
            print(self.path)
            self.wfile.write(b"Page not found - 404")
