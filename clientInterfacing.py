from socket import socket, AF_INET, SOCK_DGRAM
SERVER_IP = '192.168.137.1'
PORT_NUMBER = 5000
SIZE = 1024
print("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))
mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.connect((SERVER_IP, PORT_NUMBER))
while True:
    msgToServer = input('Enter message here: ')
    mySocket.send(msgToServer.encode())
    msgFromServer = mySocket.recv(SIZE)
    print(f"Message from Server: {msgFromServer.decode()}")
    mySocket.close()