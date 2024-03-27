# echo-client.py

import socket


def connect(ipAddress):
    HOST = ipAddress 
    PORT = 8080  
    print("g")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        data = s.recv(1024)

    print(f"Received {data!r}")