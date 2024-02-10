
import socket

# Define IP and Port for socket
localIP     = "127.0.0.1"
localPort   = 5000
sentinel = '\0'

# Create a datagram socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to address and ip
s.bind((localIP, localPort))
print("UDP server up and listening")

# Listen for incoming datagrams
buffer = {}
while True:
    bytesRecieved, address = s.recvfrom(1024)
    dataRecieved = bytesRecieved.decode('utf-8')
    
    if(dataRecieved == sentinel):
        break
    
    seqId, message = dataRecieved.split(':')
    seqId = int(seqId)
    
    buffer[seqId] = message

print('\nFragments Received:')
print(buffer)

print('\nSorting and checking for duplicates...')
sorted_buffer = dict(sorted(buffer.items()))  

# Checking for duplicates
templist = []
duplicates = []
for seqId, message in sorted_buffer.items():
    if seqId not in templist:
        templist.append(seqId)
    else:
        duplicates.append(seqId)

if (len(duplicates) > 0):
    print(f'Duplicates: {duplicates}')
else:
    print('No duplicates found')    

defraggedMessage = ''
for packet in sorted_buffer.items():
    seqId, message = packet
    seqId = int(seqId)
    defraggedMessage += message

print(f'\nThe message: {defraggedMessage}')