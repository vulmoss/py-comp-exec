#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/9/29 19:42
# @Author   : VulMoss
# @Site     : 
# @File     : p_v1.py
# @Software : PyCharm

import sys
import socket
import threading
def server_loop(local_host,local_port,remote_host,remote_port,receive_first):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        server.bind((local_host,local_port))
    except:
        print("[+] Failed to listen on %s:%d" %(local_host,local_port))
        print("[+] Check for other listening sockets or correct permissions.")
        sys.exit(0)
    print("[*] Listening on %s:%d" %(local_host,local_port))

    server.listen(5)

    while True:
        client_socket,addr = server.accept() #等待传入连接。 返回代表连接的新套接字【IP套接字，地址信息：（主机地址，端口）】以及客户端的地址
        print("[==>] Received incoming connection from %s:%d" %(addr[0],addr[1]))


