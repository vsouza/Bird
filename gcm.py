#!/usr/bin/env python
# coding: utf-8
import time
from gcm import GCM
import argparse

# API Key for your Google OAuth project
API_KEY = ''

class Gcm(object):
    """Send push notifications for Android devices"""

    number = 0

    def __init__(self):
        super(Apns, self).__init__()

    def send_push_notification(registration_id, message):
        gcm = GCM(API_KEY)
        resp = gcm.plaintext_request(registration_id=registration_id,
                                 data={'message': message})


    def send(self):
        print self.number

if __name__ == '__main__':
    x = Apns()
    x.number = 99999999
    x.send()
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--reg-id', dest='registration_id', required=True)
    parser.add_argument('-m', '--message', dest='message', required=True)
    args = parser.parse_args()
    x.send_push_notification(args.registration_id, args.message)
