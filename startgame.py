def choice():
    userChoice = input("want to be the host (1) or connect to a server (2)?")
    if userChoice == "1":
        ipServer =  input("enter ip")
        print(ipServer)
    else :
        print("start server")

choice()