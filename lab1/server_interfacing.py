import socket
port = 5000
bufferSize = 1024

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )
serverSocket.bind(('192.168.137.68', port))

print (f"Server listening on port {port}\n")

while True:
    msgFromClient, addr = serverSocket.recvfrom(bufferSize)
    print (f"Message from Client: {msgFromClient.decode()}")
    msgToClient = input('Enter message here: ')
    serverSocket.sendto(msgToClient.encode(), addr)

serverSocket.close()

