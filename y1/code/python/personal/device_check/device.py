# device.py
#
# Author: Samuel Berg
# Date: 10-Sep-2019

import socket
import uuid

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
hexIP = socket.inet_aton(IPAddr).hex()
macAddr = ':'.join(['{:02x}'.format(
    (uuid.getnode() >> elements) & 0xff)
    for elements in range(0, 2 * 6, 2)][::-1])

print("Your computer name is: " + hostname)
print("Your computer IP Address is: " + IPAddr)
print("Your hex IP Address: " + hexIP)
print("Your computer Mac Address is: " + macAddr)
