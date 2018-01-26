import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = ''
port = 1000

try:
	s.bind((host,port))
except socket.error as e:
	print(e)

s.listen(10)
conn , address = s.accept()

print('connected to:' + address[0]+':'+str(address[1]))