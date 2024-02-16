
import socket

passive_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = '127.0.0.1'
server_port = 12345

passive_socket.bind((server_ip,server_port))
passive_socket.listen(5)

print(f'Server bound to {(server_ip,server_port)} and listening:\n')

active_socket, client_address = passive_socket.accept()
print(f'Active socket address: {active_socket.getsockname()}')
print(f'Active socket peer address: {active_socket.getpeername()}')
    
while True:
    data = active_socket.recv(1024).decode()
    
    if data.lower() == 'exit':
        break
    
    print(f'Message from server: {data}')
    
    to_send = input('Enter message: ').encode()
    active_socket.send(to_send)
    
passive_socket.close()