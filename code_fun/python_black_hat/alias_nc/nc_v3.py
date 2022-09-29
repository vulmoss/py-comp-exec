#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/9/29 20:12
# @Author   : VulMoss
# @Site     : 
# @File     : nc_v3.py
# @Software : PyCharm

import sys
import socket
import threading
import getopt
import subprocess

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    print("BHP Net Tools")
    print("")
    print("Usage:nc_v3.py -t target_host -p port")
    print("-l --listen -listen on [host]:[port] for inciming connections")
    