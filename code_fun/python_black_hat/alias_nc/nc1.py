#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/9/21 15:18
# @Author   : VulMoss
# @Site     : 
# @File     : nc1.py.py
# @Software : PyCharm

import sys
import socket
import getopt
import threading
import subprocess

listen =False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port =0

def usage():
    print("BHP Net Tool")
    print("")
    print("Usage:nc1.py -t target_host -p port")
    print("-l --listen - listen on [host]:[port] for -incoming connections")

def main():
    global listen
    global port
    global execute
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()
    try :
        opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o,a in opts:
        if o in ("-h","help"):
            usage()
        elif o in ("-l","--listen"):
            listen = True
        elif o in ("-e","--execute"):
            execute =  a
        elif o in ("-c","--command"):
            command = True
        elif o in ("-u","--upload"):
            upload_destination = a
