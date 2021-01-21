#!/usr/bin/env python3
# encoding: utf-8
#__author__ == 'vulMoss'

import base64
import html
from urllib.parse import unquote

file1 = 'pwd.txt'
with open(file1) as f1:
    r1 = f1.read()
    r2 = html.unescape(r1)
#    print(r2)
    r3 = unquote(r2)
#    print(r3)
    result = base64.b64decode(r3)
    print(result.decode())
