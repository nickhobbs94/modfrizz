#!/usr/bin/python3
import socket, sys

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 502))
x = (0x0001000000060103c34f0002).to_bytes(12, byteorder='big')
print(x)
s.sendall(x)
print(s.recv(1000))

