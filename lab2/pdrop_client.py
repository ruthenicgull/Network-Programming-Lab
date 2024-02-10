import socket
import time

s = socket.socket()

server_ip = '127.0.0.1'
server_port = 2004

s.connect((server_ip, server_port))

messages = ["msg1","msg2","msg3","msg4","msg5","msg6","msg7","msg8","msg9","msg10"]

for message in messages:
    print("Sending ", message)
    s.sendto(message.encode(), (server_ip, server_port))
    serverMsg =  s.recvfrom(1024)[0]

s.close()