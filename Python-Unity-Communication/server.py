import socket

host = '127.0.0.1'
port = 12345
data = 1111
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("IP Adress: " +host)
print("Port: "+str(port))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))
s.listen(5)

conn = None

while conn == None:
	try:
		conn, addr = s.accept()
	except:
		pass

print(conn)
print(addr)

while True:
	
	try:
		data = conn.recv(2048)
		print(data)
	except Exception as e: 
		print(e)
		pass