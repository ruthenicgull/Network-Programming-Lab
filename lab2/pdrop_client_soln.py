import socket
import random
import time

server_ip = '127.0.0.1'
server_port = 12345
max_attempts = 5

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# List of messages to send
messages = ["First Message", "Second Message", "Third Message", "Fourth Message", "Fifth Message", "Sixth Message", "Seventh Message", "Eighth Message", "Ninth Message", "Tenth Message"]

for message in messages:
    attempts = 0
    while attempts < max_attempts:
        # Encode and send the message
        client_socket.sendto(message.encode('utf-8'), (server_ip, server_port))
        print(f"Sending message to server: {message}")

        try:
            # Set a timeout for receiving the acknowledgment
            client_socket.settimeout(2 ** attempts)
            
            # Wait for acknowledgment
            data, server_address = client_socket.recvfrom(1024)
            
            # If acknowledgment received, break the loop
            print(f"Acknowledgment received from server")
            break
        except socket.timeout:
            # Increment attempts and perform exponential backoff
            attempts += 1
            print(f"Timeout. Retrying (attempt {attempts})...")
            time.sleep(2 ** attempts)

    if attempts == max_attempts:
        print(f"Max attempts reached for message: {message}. Skipping.")
    else:
        print(f"Message sent successfully: {message}")

# Close the socket
client_socket.close()
