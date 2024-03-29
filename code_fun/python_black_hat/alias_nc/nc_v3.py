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
    print("-e --execute=file_to_run ")
    print("-c --command")
    print("")
    print("Examples: ")
    print("nc_v3.py -t 192.168.1.3 -p 8088 -l -c")
    print("echo ABCDEFGH | ./nc_v3.py -t 192.168.1.3 -p 8088")
    sys.exit(0)

def main():
    global listen
    global command
    global execute
    global target
    global port
    global upload_destination

    if not len(sys.argv[1:]):
        usage()

    try:
        opts,args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",["help","listen","execute","target","port","target","command","upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-l","--listen"):
            listen = True
        elif o in ("-e","--execute"):
            execute = a
        elif o in ("-c","--command"):
            command = True
        elif o in ("-u","--upload"):
            upload_destination = a
        elif o in ("-t","--target"):
            target = a
        elif o in ("-p","--port"):
            port = int(a)
        else:
            assert False,"Unhandled Option"

    if not listen and len(target) and port >0 :
        buffer = sys.stdin.read()
        client_sender(buffer)
    if listen:
        server_loop()
        main()
#当做客户端使用，发送和接受信息
def client_sender(buffer):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        client.connect((target,port))
        if len(buffer):
            client.send(buffer)
        while True:
            recv_len = 1
            response = ""
            while recv_len:
                data = client,recv(4096)
                recv_len = len(data)
                response += data
                if recv_len < 4096:
                    break
            print(response)

            buffer = raw_input("")
            buffer += "\n"
            client.send(buffer)
    except:
        print("[*] Exception! Exiting.")
        client.close()
#将命令执行输入，返回命令直接的输出
def run_command(command):
    command = command.rstrip()
    try:
        output = subprocess.check_output(command,stderr=subprocess.STDOUT,shell= True)
    except:
        output = "Failed to execute command.\r\n"
    return output

#处理连接到本服务端的客户端
def client_handler(client_socket):
    global upload
    global execute
    global command

    if len(upload_destination):
        file_buffer = ""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                file_buffer += data
        try:
            file_descriptor = open(upload_destination,"wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            client_socket.send("Successfully saved file to %s\r\n" %upload_destination)
        except:
            client_socket.send("Failed to save file to %s\r\n" %upload_destination)
    if len(execute):
        output = run_command(execute)
        client_socket.send(output)
    if  command:
        while True:
            client_socket.send("<nc:#> ")
            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)
                response = run_command(cmd_buffer)
                client_socket.send(response)



#nc 当做服务端使用
def server_loop():
    global target
    if not len(target):
        target = "0.0.0.0"
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((target,port))
    server.listen(5)

    while True:
        client_socket,addr = server.accept()
        client_thread = threading.Thread(target=client_handler,args=(client_socket,))
        client_thread.start()


if __name__ == '__main__':
    main()