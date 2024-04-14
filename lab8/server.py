import socket
import signal
import os
import select

SERVER_ADDRESS = ('127.0.0.1', 7845)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(SERVER_ADDRESS)

print('UDP echo server is listening...')
def handle_signal(sig, frame):
    print('Shutting down the server...')
    server_socket.close()
    os._exit(0)

signal.signal(signal.SIGINT, handle_signal)
server_socket.setblocking(False)
sockets = [server_socket]
while True:
    readable, _, _ = select.select(sockets, [], [])
    for sock in readable:
        if sock is server_socket:
            data, client_address = server_socket.recvfrom(1024)
            print(f"Received data from {client_address}: {data.decode()}")
            server_socket.sendto(data, client_address)
