import socket

server_ip = '127.0.0.1'
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))

server_socket.listen(5)
print(f'Server bound to {server_ip}:{server_port} and listening...')
active_socket, address = server_socket.accept()

while True:
    message = input('Enter message: ')
    active_socket.send(message.encode('utf-8'))
    if message == 'exit':
        break

server_socket.close()


