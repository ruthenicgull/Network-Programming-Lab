import socket, errno, time

sock = socket.socket()
sock.connect(('localhost', 12345))
sock.setblocking(0)

while True:
    try:
        data = sock.recv(1024)
        if not data:
            print ("connection closed")
            sock.close()
            break
        else:
            print ("Received %d bytes: '%s'" % (len(data), data))
    except socket.error as e:
        if e.args[0] == errno.EWOULDBLOCK: 
            print ('EWOULDBLOCK')
            time.sleep(1)         
        else:
            print (e)
            break
