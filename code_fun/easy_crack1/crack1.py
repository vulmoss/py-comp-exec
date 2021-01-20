#!/usr/bin/env python3
# encoding: utf-8
#__author__ == 'vulMoss'

import html
from urllib.parse import unquote

file1 = 'pwd.txt'
with open(file1) as f1:
    r1 = f1.read()
    r2 = html.unescape(r1)
    print(r2)
