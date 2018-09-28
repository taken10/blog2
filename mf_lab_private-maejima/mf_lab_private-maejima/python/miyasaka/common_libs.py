#!/usr/bin/python -tt
# -*- coding:utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys


def print_err(message, sep=' ', end='\n'):
    print(message, sep=sep, end=end, file=sys.stderr)
