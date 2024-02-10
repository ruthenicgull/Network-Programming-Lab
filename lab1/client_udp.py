import socket

msgFromClient = "Hello Server".encode()
serverIP = '127.0.0.1'
serverPort = 2000
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
UDPClientSocket.sendto(msgFromClient, (serverIP, serverPort))
msgFromServer, serverAddress = UDPClientSocket.recvfrom(bufferSize)
print(f"Message from Server: {msgFromServer.decode()}")
UDPClientSocket.close()