#!/bin/python3

from socket import *

lhost = '127.0.0.1'
lport = 1389

s = socket(AF_INET,SOCK_STREAM)
s.bind((lhost,lport))
s.listen()
conn, addr = s.accept()
print(f"[!] {addr} VULNERABLE TO LOG4SHELL")