#!/usr/bin/env python
# coding: utf-8
import time
import json
import struct
import socket
import ssl
class Apns(object):
    """Send push notifications to iOS devices."""

    number = 0
    deviceToken = None
    server = "ssl://gateway.sandbox.push.apple.com"
    port = 2195
    timeout = 6000
    keyfile = "/certificates/ios_development.cert"
    certfile = "/certificates/ios_development.cert"

    def __init__(self):
        super(Apns, self).__init__()


    def send(self, badge, message, sound):

        body = {}
        body['aps'] = {'badge':badge, 'alert': message, 'sound': sound}

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_sock = ssl.wrap_socket(s, self.keyfile, self.certfile, do_handshake_on_connect=False)

        socket.timeout(0)
        ssl_sock.setblocking(False)
        ssl_sock.connect((self.server, self.port))

        payload = json.dumps(body)
        msg = chr(0) . struct.pack('n', 32) . struct.pack('H*', deviceToken) . struct.pack('n', strlen(payload)) . payload;

        pprint.pprint(ssl_sock.getpeercert())
        ssl_sock.close()

if __name__ == '__main__':
    x = Apns()
    x.number = 99999999
    x.send(1, "teste", "default")
