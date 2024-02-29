import socket

server_ip = '127.0.0.1'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_ip, server_port))

client_socket.setblocking(True)

while True:
    message = input('Enter message: ')
    client_socket.send(message.encode('utf-8'))
    data = client_socket.recv(1024).decode('utf-8')
    if data == 'exit':
        break
    print(f'SERVER: {data}')
    

client_socket.close()


