import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from part5.rapport import Rapport
from part5.insertion import Insertion
from part5.insertion import connect_to_db

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

from urllib.parse import urlparse, parse_qs


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
        elif "/suivant" in self.path:
            query_components = parse_qs(urlparse(self.path).query)
            if not query_components:
                self.wfile.write(b'ERROR : arg missing => ?mot=string is expected')
            else:
                mot = query_components["mot"]
                rapport = Rapport(connect_to_db('insertion.sql'), self.wfile)
                dict_of_following_words = rapport.get_most_used_following_word(mot[0])
                most_used_following_word = rapport.get_first_value_from_dict(dict_of_following_words)
                rapport.print_value(most_used_following_word)
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
            l = []
            print(list_values)
            for value in list_values[0].split():
                l.append(value)
            for i in range(0, len(l)):
                if i == len(l) - 1:
                    following_word = ""
                else:
                    following_word = str(l[i + 1])

                insertion.write_in_db(str(l[i]), following_word)


def run(server_class=HTTPServer, handler_class=Server):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    print("Server running at localhost:8080...")
    httpd.serve_forever()


run()
