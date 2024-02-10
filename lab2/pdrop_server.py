import socket
import random
import time

ip = '127.0.0.1'
port = 2004
addressFamily = socket.AF_INET
transmissionProtocol = socket.SOCK_DGRAM
s = socket.socket(addressFamily,transmissionProtocol)
print(f"Address Family: {addressFamily}")
print(f"Transmission Medium: {transmissionProtocol}")

print(f"Socket bound to ({ip},{port})")

s.listen(10)

while True:
    try:
        data, addr = s.recvfrom(1024).decode()
        if(random.random() > 0.7):
            print("Recieving")
            print('Received from client:', data)
            dropMessage = 'Received'
            s.sendto(dropMessage.encode(), addr)
        else:
            s.sendto('NA'.encode(), addr)
            print("packet dropped") 
    except KeyboardInterrupt:
        break
s.close()