#!/usr/bin/env python3
# encoding: utf-8
#__author__ == 'vulMoss'

import base64
import html
from urllib.parse import unquote


def read_file():
    file1 = 'pwd.txt'
    with open(file1) as f1:
        return f1.read()

def Html_crack(raw_data):
    return html.unescape(raw_data)

def Url_crack(raw_data):
    return unquote(raw_data)

def Bs64_crack(raw_data):
    return base64.b64decode(raw_data).decode()



if __name__ == '__main__':
    result_html = Html_crack(read_file())
    result_url = Url_crack(result_html)
    result_base64 = Bs64_crack(result_url)
    print(result_base64)
