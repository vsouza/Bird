#!/usr/bin/env python
# coding: utf-8
import time

class Apns(object):
    """Send push notifications to iOS devices."""

    number = 0

    def __init__(self):
        super(Apns, self).__init__()


    def send(self):
        print self.number

if __name__ == '__main__':
    x = Apns()
    x.number = 99999999
    x.send()
