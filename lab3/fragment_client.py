
import socket
import random

# Function to convert message to list of fragments
def toFragments(message, MAX_PACK):
    startSeqId = random.randint(100,900)
    fragments = []
    i = 0
    while i < len(message):
        fragment = {
            'seqId': startSeqId, 
            'data': message[i: i + MAX_PACK]
        }
        fragments.append(fragment)
        startSeqId += 1
        i += MAX_PACK
    return fragments
        

MAX_PACK = 4
server_ip = '127.0.0.1'
port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sentinel = '\0'

while True:
    message = input('Enter message here:')
    # Convert to list of fragments
    fragments = toFragments(message, MAX_PACK)

    # Sending fragments one by one
    for fragment in fragments:
        sequenceNumber = fragment['seqId']
        data = fragment['data']
        msgToSend = f'{sequenceNumber}:{data}'
        client.sendto(msgToSend.encode('utf-8'), (server_ip, port))
        
    # Sending a sentinel
    client.sendto(sentinel.encode('utf-8'), (server_ip, port))



    
    
    


