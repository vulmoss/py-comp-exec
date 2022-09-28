#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/9/28 13:20
# @Author   : VulMoss
# @Site     : 
# @File     : getopt_v1.py
# @Software : PyCharm

import socket
import sys
import getopt
import threading
import subprocess

# 定义一些全局变量
LISTEN   = False
COMMAND  = False
UPLOAD   = False
EXECUTE  = ''
TARGET   = ''
UP_DEST  = ''
PORT     = 0

# 帮助选项
def usage(): #打印所有的提示
    print( "Usage: nc.py -t <HOST> -p <PORT>")
    print ("  -l --listen                  listen on HOST:PORT")
    print ("  -e --execute=file            execute the given file")
    print ("  -c --command                 initialize a command shell")
    print ("  -u --upload=destination      upload file and write to destination")
    print ("")
    print ("Examples:")
    print ("netcat.py -t localhost -p 5555 -l -c")
    print ("netcat.py -t localhost -p 5555 -l -u=target")
    print ("netcat.py -t localhost -p 5555 -l -e=\"cat /etc/passwd\"")
    print ("echo 'ABCDEFGHI' | ./netcat.py -t localhost -p 8088")
    sys.exit(0)

# 服务端函数,与上篇中的 TCP 服务端还是很相似的
def server_loop():  #定义一个服务端
    server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    server.bind(( TARGET, PORT )) #绑定的ip和端口号
    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        # 分拆一个线程处理新的客户端
        client_thread = threading.Thread( target =client_handler, args=(client_socket,))
        client_thread.start()
#服务端接受ip和端口的发送的信息
# 客户端函数,与上文中那个简易版的 netcat 有些相似,创建套接字然后进入循环收发数据
def client_sender(buffer): #客户端
    client = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) #套接字，服务器之间通信，tcp

    try:
        # 连接到目标主机
        client.connect(( TARGET, PORT ))

        # 检测是否收到数据
        if len(buffer): #如果有收到数据
            client.send(buffer) #客户端把数据发送

        while True:
            # 等待数据
            recv_len = 1
            response = ''

            while recv_len:
                data = client.recv(4096) #客户端接受数据
                recv_len = len(data)
                response += data
                if recv_len < 4096:
                    break
            print (response)

            # 等待更多数据,直到没有新的数据
            buffer = raw_input('') #输入
            buffer += '\n'   #输入的数据然后下一行

            client.send(buffer)

    except:
        print('[*] Exception. Exiting.')
        client.close()


# 实现文件上传,命令执行以及与 shell 相关的功能(在一个名为 NETCAT 的特殊 shell)
def client_handler(client_socket):
    global UPLOAD
    global EXECUTE
    global COMMAND

    # 检测上传文件
    if len(UP_DEST):
        file_buf = ''

        # 读取数据,直到没有新的数据
        while 1:
            data = client_socket.recv(1024)
            if data:
                file_buffer += data
            else:
                break

        # 以二进制的方式写入字节
        try:
            with open(UP_DEST, 'wb') as f: #以写以及二进制的方式打开f
                f.write(file_buffer) #将file_buffer写入f文件
                client_socket.send('File saved to %s\r\n' % UP_DEST)
        except:
            client_socket.send('Failed to save file to %s\r\n' % UP_DEST)

    # 检测可执行命令:
    if len(EXECUTE):
        output = run_command(EXECUTE)
        client_socket.send(output)

    # 如果请求 shell,则进入循环
    if COMMAND:
        while True:
            # 显示命令提示符:
            client_socket.send('[NETCAT_Liu]# ')
            cmd_buffer = ''

            # 扫描换行符以确定何时执行命令
            while '\n' not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)

            # 回传命令输出
            response = run_command(cmd_buffer)
            client_socket.send(response)

def run_command(command):
    command = command.rstrip()
    print (command)
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
       output = "Failed to execute command.\r\n"
    return output

def main():
    global LISTEN
    global PORT
    global EXECUTE
    global COMMAND
    global UP_DEST
    global TARGET

    if not len(sys.argv[1:]):
        usage()

    # 读取命令行选项
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu", \
            ["help", "LISTEN", "EXECUTE", "TARGET", "PORT", "COMMAND", "UPLOAD"])
    except getopt.GetoptError as err:
        print (str(err))
        usage()

    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
        elif o in ('-l', '--listen'):
            LISTEN = True
        elif o in ('-e', '--execute'):
            EXECUTE = a
        elif o in ('-c', '--commandshell'):
            COMMAND = True
        elif o in ('-u', '--upload'):
            UP_DEST = a
        elif o in ('-t', '--target'):
            TARGET = a
        elif o in ('-p', '--port'):
            PORT = int(a)
        else:
            assert False, "Unhandled option"

    # NETCAT Client
    if not LISTEN and len(TARGET) and PORT > 0:
        # 从命令行读取内存数据
        # 这里会阻塞,所以不在向标准输入发送数据时要发送 CTRL - D
        buffer = sys.stdin.read()

        # 发送数据
        client_sender(buffer)

    # NETCAT Server
    if LISTEN:
        if not len(TARGET):
            TARGET = '0.0.0.0'
        server_loop()

if __name__ == '__main__':
    main()