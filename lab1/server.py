import socket

ip = '127.0.0.1'
port = 1060
addressFamily = socket.AF_INET
transmissionProtocol = socket.SOCK_STREAM
s = socket.socket(addressFamily, transmissionProtocol)
print("Address Family: ",addressFamily)
print("Transmission Medium: ",transmissionProtocol)
s.bind((ip, 1060))
print("Socket bound to (", ip,", ",1060, ")")

s.listen(2)

while True:
    ct_s, addr = s.accept()     
    print('Got connection from', addr)
    client_ip = ct_s.getpeername()[0]
    print('Client IP address:', client_ip)
    data = ct_s.recv(1024).decode()
    print('Received from client:', data)
    response = 'HELLO CLIENT'
    ct_s.send(response.encode())
    ct_s.close()



