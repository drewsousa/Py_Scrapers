# DFS - Basic Python port scanner
# Interpreter: Python 3.9
# Packages: pip v21.3.1, setuptools v60.2.0, wheel v0.37.1

import socket
import subprocess
import sys
from datetime import datetime

# Clear the terminal screen
subprocess.call('clear', shell=True)

# Ask for input on IP to scan
# TODO import IP list from .txt or .json file
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print banner
print("_" * 60)
print("Scanning host(s)", remoteServerIP)
print("_"*60)

# Date and time scan starts
dt1 = datetime.now()

# Using the range function to specify ports with some error handling
try:
    for port in range(1, 5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:        Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("Ctrl+C Pressed. Exiting")
    sys.exit()

except socket.gaierror:
    print("Could not resolve Hostname. Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to server. Exiting")
    sys.exit()

# Checking time again
dt2 = datetime.now()

# Calculate the difference in time to now how long the scan took
total = dt2 - dt1

# Ending by printing time for scan to run
print('Scanning Completed in: ', total)
