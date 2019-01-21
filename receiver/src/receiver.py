#! /usr/bin/env python
"""Receive HTTP messages
"""

import sys
import logging
import coloredlogs
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from io import BytesIO
from cryptography.fernet import Fernet
import time

logger = logging.getLogger()
coloredlogs.install(level='DEBUG')

class StoreData(object):
    def __init__(self):
        """Class constructor.
        """
        self.key = 'AQZKgmen1zFKjyi0_IYvGb46P2F5ieNxm3qkHwzn4pg='

    def execute(self, text_data):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        with open("/work/file-" + timestr + ".xml", "w") as text_file:
            text_file.write(text_data)

class Decrypt(object):
    def __init__(self):
        """Class constructor.
        """
        self.key = 'AQZKgmen1zFKjyi0_IYvGb46P2F5ieNxm3qkHwzn4pg='

    def execute(self, text_data):
        cipher_suite = Fernet(self.key)
        decrypted = cipher_suite.decrypt(text_data)
        return decrypted


class ServerHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        decrypted = Decrypt().execute(post_body)
        StoreData().execute(decrypted)
        logger.debug(decrypted)
        self.send_response(204)
        self.end_headers()
        
def run(server_class=HTTPServer, handler_class=ServerHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logger.info('Started httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()