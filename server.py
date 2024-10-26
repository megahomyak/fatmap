from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3

class FatMapServer(BaseHTTPRequestHandler):
    def get_layer(self):
        pass

    def get_value(self):
        print(self.rfile.read())

    def add_layer(self):
        pass

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        {
            "/get_layer": self.get_layer,
            "/get_value": self.get_value,
            "/add_layer": self.add_layer,
        }[self.path]()
        self.wfile.write(b'Hello, World!')

httpd = HTTPServer(('', 8000), FatMapServer)
httpd.serve_forever()
