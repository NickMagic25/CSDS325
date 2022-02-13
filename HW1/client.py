#Nick Majkic
#CSDS 325

from socket import *


def help():
    return """
    help 
    get key 
    put key value 
    values 
    keyset 
    mappings 
    bye """


def connect():
    print("Welcome to the KeyValue Service Client")
    serverName=raw_input("Type server name or IP address: ")
    serverPort=12000
    clientSocket=socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    loop=True
    while loop:
        command=raw_input("KeyValue Service> ")
        if command.lower() == "bye":
            clientSocket.close()
            loop=False
            print("See you later.")
        elif command.lower() == "help":
            print(help())
        else:
            clientSocket.send(command.encode())
            serverOuput=clientSocket.recv(1024)
            print(serverOuput.decode())


connect()