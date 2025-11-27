# client.py
# A simple client to connect to the secure caching service.

import socket

HOST = '127.0.0.1'
PORT = 65432

def main():
    """
    Connects to the server and sends a sample message.
    """
    print("Initializing client...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # TODO: Phase 2 - Implement the client-side secure handshake and encryption.
        
        # TODO: Implement client logic to send SET, GET, DELETE commands.
        
        print("Sending sample message...")
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    print('Received', repr(data))

if __name__ == "__main__":
    main()
