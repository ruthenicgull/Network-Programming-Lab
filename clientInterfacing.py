import socket
c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_ip = "192.168.137.42"
server_port = 5000

while True:
    msg = input("Enter the message: ")
    c.sendto(msg.encode(),(server_ip, server_port))
    rec_data,rec_address = c.recvfrom(1024)
    print("Message from server: ",rec_data.decode())

c.close()