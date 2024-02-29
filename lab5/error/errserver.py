import socket
import errno

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)

    print("Server listening...")

    while True:
        try:
            client_socket, address = server_socket.accept()
            print(f"Connection from {address} established.")

            data = client_socket.recv(1024)	
            while data:			        
               print (data.decode())
               data = client_socket.recv(1024)

            client_socket.sendall(b"Message received by server.")

            client_socket.close()

        except socket.error as e:
            if e.errno == errno.ENOBUFS:
                print("No buffer space available.")
            elif e.errno == errno.EADDRNOTAVAIL:
                print("The requested address is not available.")
            elif e.errno == errno.EADDRINUSE:
                print("The address is already in use.")
            elif e.errno == errno.EAFNOSUPPORT:
                print("The specified address family is not supported.")
            elif e.errno == errno.ECONNRESET:
                print("Connection reset by peer.")
            elif e.errno == errno.EHOSTUNREACH:
                print("No route to the host.")
            elif e.errno == errno.ENETDOWN:
                print("Network is down.")
            elif e.errno == errno.ENETRESET:
                print("Network dropped connection on reset.")
            elif e.errno == errno.ENETUNREACH:
                print("Network is unreachable.")
            elif e.errno == errno.EWOULDBLOCK:
                print("Network is unreachable #uska phone bhi yahi kehta tha.")
            elif e.errno == errno.ESHUTDOWN:
                print("Cannot send after socket shutdown.")
            elif e.errno == errno.ETIMEDOUT:
                print("Connection timed out.")
            else:
                print("Socket error:", e)

    server_socket.close()

server()