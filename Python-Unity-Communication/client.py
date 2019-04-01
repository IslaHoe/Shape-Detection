import socket

host = '127.0.0.1'
port = 12345
data = 0
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("IP Adress: " +host)
print("Port: "+str(port))

s.connect((host,port))

while True:
	if input("->")=="exit":
		break;
	datasent=str.encode(input("->"))
	s.send(datasent)
		#print(sent)