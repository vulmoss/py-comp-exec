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


def hexdump(sec,length = 16):
    result = []
    digits = 4 if isinstance(src,unicod) else 2
    for i in xrange(0,len(src),length):
        s = src[i:i+length]
        hexa = b' '.join(["%0*X" %(digits,ord(x)) for x in s])
        text = b''.join([x if 0x20 <= ord(x) <0x7F else b'.' for x in s])
        result.append(b"%04X %-*s %s" %(i,length*(digits + 1),hexa,text))
    print(b'\n'.join(result))

def request_handler(buffer):
    return buffer

def response_handler(buffer):
    return buffer

def receive_from(connection): #这个入参是什么意思??
    buffer = ""

    connection.settimeout(5)#超过5秒 超时
    try:
        while True:
            data = connection.recv(4096) #不断接受数据 赋值给data
            if not data:
                break
            buffer += data
    except:
        pass
    return buffer #最后返回所有的接受的数据

def proxy_handler(client_socket,remote_host,remote_port,receive_first):
    remote_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #目标socket
    remote_socket.connect((remote_host,remote_port))
    if receive_first :
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

        remote_buffer = response_handler(remote_buffer)

        if len(remote_buffer):
            print("[<==] sending %d bytes to localhost." % len(remote_buffer))
            client_socket.send(remote_buffer)
    while True:
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            print("[==>] receiving %d bytes to " %len(local_buffer))
            hexdump(local_buffer)
            local_buffer = request_handler(local_buffer)

            remote_socket.send(local_buffer)
            print("[==>] send to remote.")

    remote_buffer = receive_from(remote_socket)

    if remote_buffer :
        remote_buffe

def server_loop(local_host,local_port,remote_host,remote_port,receive_first): #服务端的配置
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建一个socket
    try:
        server.bind((local_host,local_port)) #绑定ip和端口
    except:
        print("[+] Failed to listen on %s:%d" %(local_host,local_port))
        print("[+] Check for other listening sockets or correct permissions.")
        sys.exit(0)
    print("[*] listening on %s:%d" %(local_host,local_port))

    server.listen(5) #开始监听

    while True:
        client.socket,addr = server.accept() #服务端接受了信息
        print("[==>] Received incoming connection for %s:%d" %(addr[0],addr[1])) #打印客户端的ip和端口
        proxy_thread = threading.Thread(target=proxy_handler,args=(client_socket,remote_host,remote_port,receive_first)) #调用了proxy_handler
        proxy_thread.start()



def main():
    if len(sys.argv[1:]) != 5:
        print("Usage:./p_v1.py [localhost][localport][remotehost][remoteport][recive_first]")
        print("Example :./p_v1.py 127.0.0.1 9000 10.12.132.1 9000 True")
        sys.exit(0)

    local_host = sys.argv[1]
    local_port = sys.argv[2]

    remote_host = sys.argv[3]
    remote_port = sys.argv[4]
    receive_first = sys.argv[5]

    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False

    server_loop(local_host,local_port,remote_host,remote_port,receive_first)



if __name__ == '__main__':
    main()