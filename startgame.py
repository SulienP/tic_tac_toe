import connect, server
def choice():
    userChoice = input("want to be the client (1) or host a server (2)?\n")
    if userChoice == "1":
        # ipServer =  input("enter ip\n")
        connect.connect()
    else :
       server.server()

choice()