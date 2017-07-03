import socket
import sys
import select
from thread import *

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

if len(sys.argv)!=3:
	print "Correct usage:script,IP address,port number"
	exit()

IP_address=str(sys.argv[1])
Port=int(sys.argv[2])

server.bind((IP_address,Port))
server.listen(100)

conn ,addr=server.accept()
print addr[0]+" connected"
conn.send("Welcome to my chatroom!")
while True:
	try:
		message=conn.recv(2048)
		if message:
			print "<client says >"+message
			message=raw_input('Enter message:')
			conn.send(message)
		else:
				break
	except:
			continue
conn.close()
server.close()