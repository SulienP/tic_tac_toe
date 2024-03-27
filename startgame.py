import connect, server
def choice():
    userChoice = input("want to be the client (1) or connect to a server (2)?\n")
    if userChoice == "1":
        ipServer =  input("enter ip\n")
        connect.connect(ipServer)
    else :
       server.server()

choice()