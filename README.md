![image](https://user-images.githubusercontent.com/96201375/146281662-d4ff036b-2b33-4148-a8a7-ca84bbd194ba.png)

# Requirements
```python
python -m pip install requests
```
# Notes
The log4shell listener must be on the same subnet as the scanner, otherwise you'll need to forward the ports accordingly within your network. An easy alternative to this is running the listener on an azure/aws vm and ensuring the appropriate port (1389 by default) is accessible from the internet.

# Syntax
```python
log4shell_scanner.py <http(s)://ip_or_hostname[:port]> <listener_ip>
```
```python
log4shell_listener.py <listener_ip>
```
