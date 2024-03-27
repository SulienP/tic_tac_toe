import socket
import pickle

def server():
    HOST = "10.44.18.213"
    PORT = 8080
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if data == b'quit':
                    break
                print(pickle.loads(data))
                
                userChoice = input("enter coordinate?\n")
                conn.sendall(bytes(userChoice, 'utf-8'))