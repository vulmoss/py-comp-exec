#!/usr/bin/env python3
# encoding: utf-8
#__author__ == 'vulMoss'


import socket

def socket_send(command):
    target_host = '127.0.0.1'
    target_port = 8088

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    client.connect((target_host,target_port))

    client.send(command.encode('utf-8'))

    reslut = client.recv(4096)
    return reslut


if __name__ == '__main__':
    print(socket_send('ls').decode())
