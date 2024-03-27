import socket
import pickle
import random

def server():
    HOST = "10.44.18.213"
    PORT = 8080
    playing = True
    tab = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            
            if random.randint(0,1) == 0:
                print("le server commence")
                userChoice = input("enter coordinate?\n")
                if userChoice == "quit":
                    playing = False
            else:
                print("le client commence")
                conn.sendall(pickle.dumps(tab))
            while playing:
                data = conn.recv(1024)
                if data == b'quit':
                    break
                print(pickle.loads(data))
                
                userChoice = input("enter coordinate?\n")
                if userChoice == "quit":
                    break
                conn.sendall(pickle.dumps(tab))