import socket
import random

# Server configuration
server_ip = '127.0.0.1'
server_port = 12345

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

print(f"UDP server is listening on {server_ip}:{server_port}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    
    # Simulate packet dropping with 70% probability
    if random.random() < 0.7:
        print("Packet dropped!")
        continue

    print(f"Received message from {client_address}: {data.decode('utf-8')}")

    # Send acknowledgment back to the client
    acknowledgment = "Message received successfully"
    server_socket.sendto(acknowledgment.encode('utf-8'), client_address)
