import socket

# Define IP and Port for socket
localIP     = "127.0.0.1"
localPort   = 2000
bufferSize  = 1024

msgFromServer       = "Hello Client".encode()
# Create a datagram socket
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

# Listen for incoming datagrams
while(True):
    clientMsg, clientAddress = UDPServerSocket.recvfrom(bufferSize)
    print(f"Message from Client: {clientMsg.decode()}")
    print(f"Client IP Address: {clientAddress}")
    # Sending a reply to client
    UDPServerSocket.sendto(msgFromServer, clientAddress)
UDPServerSocket.close()