# it's important to run the server before the client

import socket

#localhost adress, the server host
host = '127.0.0.1'
#port you will use for the server communication, use comething with 5 digits to avoid conflicts, like 12345
port = 12345

#create socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("IP Adress: " +host)
print("Port: "+str(port))

#connect to the server. The server has to accept the connection.
s.connect((host,port))

while True:
	#if you want to exit the loop and end the software
	if input("->")=="exit":
		break;
	#data you want to send to the server you are connected
	datasent=str.encode(input("->")) #the data need to be encoded
	s.send(datasent)
		#print(sent)