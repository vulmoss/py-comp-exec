#!/usr/bin/env python3
# encoding: utf-8
#__author__ == 'vulMoss'

import socket

target_host = "127.0.0.1"
target_port = 8088

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send("HAHAHA".encode())

response = client.recv(4096)
