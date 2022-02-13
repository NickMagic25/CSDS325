#Nick Majkic
#CSDS 325
import socket
from socket import *

# just to make it easier to get the string #
def help():
    return """
    help 
    get key 
    put key value 
    values 
    keyset 
    mappings 
    bye """


def main():
    print("Welcome to the KeyValue Service Client")
    # taken from chapter 2 slides #
    try:
        serverName=raw_input("Type server name or IP address: ")
        serverPort=12000
        clientSocket=socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        loop = True  # the loop will always run while loop is true #
        print("Connected to " + serverName + "!")
        while loop:
            command = raw_input("KeyValue Service> ")
            if command.lower() == "bye":  # check if bye was sent #
                clientSocket.send(command.lower().encode())
                clientSocket.close()  # close the connection #
                loop = False  # terminate the loop #
                print("See you later.")
            elif command.lower() == "help":  # check if help was sent #
                print(help())
            else:  # else send the command to the server
                clientSocket.send(command.encode())
                serverOuput = clientSocket.recv(1024)
                print(serverOuput.decode())
    except gaierror:  # if the server name/IP address is invalid catch the error and run main again #
        print("Invalid server name or IP address \n")
        main()


main()  # run main function #
