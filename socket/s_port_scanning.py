import socket

# print(s)
#server = '198.54.125.88'
server = 'pythonprogramming.net'
#server = '127.0.0.1'
def portscan(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(.8)
    try:
        s.connect((server,port))
        return True
    except:
        return False

for p in range(18,25):
	if portscan(p):
		print("Port is open:"+str(p))
	else:
		print("This port is close"+str(p))

# print(pscan(80))
