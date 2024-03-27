# echo-client.py

import socket
import pickle

def connect():
    HOST = "10.44.18.213"
    PORT = 8080
    tab = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            userChoice = input("enter coordinate?\n")
            if userChoice == "quit":
                break
            s.sendall(pickle.dumps(tab))
            data = s.recv(1024)
            print(data.decode('utf-8'))
            

    print(f"Received {data!r}")