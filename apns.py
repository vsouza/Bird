#!/usr/bin/env python
# coding: utf-8
import json
import struct
import socket
import ssl
import binascii
import config
import click

deviceToken = config.device_token
pushServer = "gateway.sandbox.push.apple.com"
port = 2195
keyfile = config.certificates_dir + "/key.pem"
certfile = config.certificates_dir + "/pushcert.pem"


@click.command()
@click.option('--badge', default='1', help='Number of notification.')
@click.option('--message', default="test message", help='string of message')
@click.option('--sound', default="default", help='what sound you want?')
def send(badge, message, sound):

    body = {}
    body['aps'] = {'badge':badge, 'alert': message, 'sound': sound}

    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)

    s.connect((pushServer, port))
    ssl_sock = ssl.wrap_socket(s, keyfile, certfile)
    ssl_sock.setblocking(False)

    payload = json.dumps(body)
    
    token = binascii.unhexlify(deviceToken)
    fmt = '!cH32sH{0:d}s'.format(len(payload))
    cmd = '\x00'
    message = struct.pack(fmt, cmd, len(token), token, len(payload), payload)
    ssl_sock.write(message)
    
    ssl_sock.close()
    
    return True

if __name__ == '__main__':
    send()
