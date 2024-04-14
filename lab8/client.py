import socket
import signal
import os
import select

SERVER_ADDRESS = ('127.0.0.1', 7845)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def handle_signal(sig, frame):
    print('Closing the client...')
    client_socket.close()
    os._exit(0)

signal.signal(signal.SIGINT, handle_signal)
client_socket.setblocking(False)
sockets = [client_socket]
while True:
    _, writable, _ = select.select([], sockets, [])
    for sock in writable:
        if sock is client_socket:
            message = input("Enter message: ")
        if message.lower() == 'exit':
            client_socket.close()
            os._exit(0)
            
    client_socket.sendto(message.encode(), SERVER_ADDRESS)

readable, _, _ = select.select(sockets, [], [])
for sock in readable:
    if sock is client_socket:
        echoed_message, server_address = client_socket.recv
        print(f"Received echo from server {server_address}: {eschoed_message}")