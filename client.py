import socket,sys,time
s=socket.socket()
host=input(str('Enter host: '))
port=8080
s.connect((host,port))
print('Connected to server')
while 1:
	incmmsg=s.recv(1024)
	incmmsg=incmmsg.decode()
	print('Server:',incmmsg)
	print('')
	message=input(str('>>'))
	message.encode()
	conn.send(message)
	print('msg sent')
	print('')
	
	
