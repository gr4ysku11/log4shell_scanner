#!/bin/python3
# log4shell_listener.py <listener_ip>

import sys
from socket import *

lip = '127.0.0.1'
lport = 1389

s = socket(AF_INET,SOCK_STREAM)
s.bind((lip,lport))
s.listen()
conn, addr = s.accept()
print(f"[!] {addr} VULNERABLE TO LOG4SHELL")