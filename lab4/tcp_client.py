import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = '127.0.0.1'
server_port = 12345

client_socket.connect((server_ip, server_port))

print(f"Client socket name: {client_socket.getsockname()}")
print(f"Client peer name: {client_socket.getpeername()}")

while True:
    to_send = input('Enter message: ').encode()
    client_socket.send(to_send)
    
    data = client_socket.recv(1024).decode()
    if data.lower() == 'exit':
        break
    
    print(f'Message from client: {data}')
    
    