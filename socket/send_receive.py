import socket
import sys
from _thread import *

host = ''
port  = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((host,port))
except socket.error as e:
	print(e)

s.listen(10)
data =''
def threaded_clint(conn):
	conn.send(str.encode('Welcome to the server\n'))
	while True:
		data = conn.recv(2048)
		reply = 'Server message: '+data.decode()
		
		print(data.decode())
		if not data:
			break
		conn.sendall(str.encode(reply))
	conn.close()
while True:
	conn, addr = s.accept()
	print('connected to: ',addr[0]+':'+str(addr[1]))
	start_new_thread(threaded_clint,(conn,))
	print(conn)
