# it's important to run the server before the client

import socket

#server and client adress(host,port) need to be the same
#localhost adress
host = '127.0.0.1'
#port you will use for the server communication, use comething with 5 digits to avoid conflicts, like 12345
port = 12345

data = 1111

print("IP Adress: " +host)
print("Port: "+str(port))

#create the socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#this line above make this code the server
s.bind((host,port))
#Number of connected clients, I put 5, but i think 1 works too. We only need one client.
s.listen(5)

#now we enter in this loop until the client try to connect. So we accept.
conn = None

while conn == None:
	try:
		conn, addr = s.accept()
	except:
		pass
#test
print(conn)
print(addr)

#main loop
while True:
	
	try:
		data = conn.recv(2048) #get the data from the client
		print(data)
	except Exception as e: 
		print(e)
		pass