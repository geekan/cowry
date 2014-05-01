#!/usr/bin/env python

import os

if ord(os.urandom(1)) > 0x7f:
    with open(__file__, 'rb') as fp:
        print fp.read()
else:
    os.remove(__file__)
