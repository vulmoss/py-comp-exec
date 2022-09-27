#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/9/27 21:45
# @Author   : VulMoss
# @Site     : 
# @File     : get_opt2.py
# @Software : PyCharm

import getopt
import sys

opts,args = getopt.getopt(sys.argv[1:],"-h-f:v",["--help","--version","--filename="])
for opt,a in opts:
    if opt in ("-h","--help"):
        print("[+] this is help info")
        exit(1)
    if opt in ("-v","--version"):
        print("[+] version is 1.0")
        exit(1)
    if opt in ("-f","--filename"):
        fileN = a
        print("[+] filename is ",fileN)
        exit(1)
