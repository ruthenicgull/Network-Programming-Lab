import socket

s = socket.socket()
server_ip = '127.0.0.1'
server_port = 1060
s.connect((server_ip, server_port))
s.send('HELLO SERVER'.encode())
data = s.recv(1024).decode()
print('Received from server:', data)
s.close()