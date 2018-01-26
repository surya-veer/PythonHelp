import socket
 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print(s)

server = 'vimshan.com'
server_ip = socket.gethostbyname(server)
port = 80
print(server_ip)

request = 'GET / HTTP/1.1\nHost:'+server+'\n\n'

s.connect((server,port))
s.send(request.encode())
result = s.recv(4096)

print(result)

