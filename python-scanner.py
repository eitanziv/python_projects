#!/usr/bin/env python3
import sys
import socket

if lend(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else
	print("Invalid amound of arguments")

print("-" * 50)
print("Scanning: " + target)
print("-" * 50)

try:
	for port in range(1,65535):
		s = socket.setdefaulttimeout(1)
		socket.setdefaulttimeout(1)

		result = s.connect_ex((target,port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
		print("\n Exciting")
		sys.exit()
except socket.gaierror:
		print("\n Hostname could not resolved")
		sys.exit()
except socket.error:
		print("\ Server not responding")
		sys.exit()
