import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from part4.rapport import Rapport
from part4.insertion import Insertion
from part4.insertion import connect_to_db

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        self._set_headers()
        if self.path == "/rapport":
            rapport = Rapport(connect_to_db('insertion.sql'), self.wfile)
            rapport.run()
        else:
            self.wfile.write(b'non')

    def do_POST(self):
        self._set_headers()
        if self.path == "/integration":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            values = body.decode("utf-8")
            list_values = [values]
            insertion = Insertion(connect_to_db('insertion.sql'))
            for value in list_values[0].split():
                insertion.write_in_db(value)


def run(server_class=HTTPServer, handler_class=Server):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    print("Server running at localhost:8080...")
    httpd.serve_forever()


run()
