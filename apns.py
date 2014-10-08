#!/usr/bin/env python
# coding: utf-8
import json
import struct
import socket
import ssl
import binascii
import config

class Apns(object):
    """Send push notifications to iOS devices."""

    deviceToken = config.device_token
    pushServer = "gateway.sandbox.push.apple.com"
    port = 2195
    keyfile = config.certificates_dir + "/key.pem"
    certfile = config.certificates_dir + "/pushcert.pem"

    def __init__(self):
        super(Apns, self).__init__()


    def send(self, badge, message, sound):

        body = {}
        body['aps'] = {'badge':badge, 'alert': message, 'sound': sound}

        s = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

        s.connect((self.pushServer, self.port))
        ssl_sock = ssl.wrap_socket(s, self.keyfile, self.certfile)
        ssl_sock.setblocking(False)

        payload = json.dumps(body)
        
        token = binascii.unhexlify(self.deviceToken)
        fmt = '!cH32sH{0:d}s'.format(len(payload))
        cmd = '\x00'
        message = struct.pack(fmt, cmd, len(token), token, len(payload), payload)
        ssl_sock.write(message)
        
        ssl_sock.close()
        
        return True

if __name__ == '__main__':
    push = Apns()
    push.send(1, "teste", "default")
