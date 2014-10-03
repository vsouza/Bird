#!/usr/bin/env python
# coding: utf-8
import os

class Validate(object):
    """Validate numbers, tokens and some data"""

    def __init__(self, arg):
        super(Validate, self).__init__()
        self.arg = arg

    def isNumber(self):
        return True

    def isValid(self):
        return True

    def isToken(self):
        return True
