#!/usr/bin/env python

import pyfiglet
import sys
import socket
from api.portscan import PortUtil

ascii_banner = pyfiglet.figlet_format("ipTool")
print(ascii_banner)

if len(sys.argv) == 3:
    action = sys.argv[1]
    target = socket.gethostbyname(sys.argv[2])
elif len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")

print("-" * 50)
print("Scanning Target: " + target)
print("-" * 50)

if action == "-p":
    print("Starting Portscan (1->1024)...")
    PortUtil.scanOpenPorts(target=target, r=range(1, 1024))
elif action == "-pA":
    print("Starting Portscan (1->65536)...")
    PortUtil.scanOpenPorts(target=target, r=range(1, 65536))
elif action == "-L":
    print("Starting Lookup...")
else:
    print("Invalid action.")
