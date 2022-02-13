#Nick Majkic
#CSDS 325
from socket import *


store_inventory={}  # store inventory for the whole program #


# get function, get value for a given key #
def get(key):
    if key in store_inventory:
        return str(store_inventory[key])
    else:
        return "Cannot find \"" + key + "\" in the data store."


# put function, maps a key to a value #
def put(key,value):
    store_inventory[key]=value
    return "Successfully mapped \""+ str(value) + "\" to \"" + key + "\"."


# returns the keys with their values #
def mappings():
    output=""
    for key in list(store_inventory):
        output+= key + " " + str(store_inventory[key]) + "\n"
    return output


# returns all keys #
def key_set():
    output=""
    for key in list(store_inventory):
        output+=key + "\n"
    return output


# returns all values #
def values():
    output = ""
    for key in list(store_inventory):
        output += str(store_inventory[key]) + "\n"
    return output


# handles user input #
def handler(arr):
    if len(arr) == 3:
        if arr[0].lower() == "put":
            try:  # map arr[2] to arr[1] if arr[2] is an int
                return put(arr[1], int(arr[2]))
            except ValueError as e:  # catch ValueError in case arr[2] is not an int #
                return "\"" + arr[2] + "\" is not a valid value"
    elif len(arr) == 2:
        if arr[0].lower() == "get":
            return get(arr[1])  # get the value at arr[1]#
    elif len(arr)==1:
        if arr[0].lower() == "values":
            return values()  # get all values #
        elif arr[0].lower() == "keyset":
            return key_set()  # get the keyset #
        elif arr[0].lower() == "mappings":
            return mappings()  # get the mappings #
    return "Invalid command"  # whatever was entered is an invalid command #


def connected(serverSocket):
    connectionSocket, addr = serverSocket.accept()
    loop = True
    try:
        while loop:  # always run the loop #
            sentence = connectionSocket.recv(1024).decode()
            print("Received: " + sentence)  # prints everything recieved, makes checking for errors easier #
            arr = sentence.split()
            if arr[0].lower() == "bye":  # check if input was bye #
                connectionSocket.close()
            else:  # else handle the input #
                connectionSocket.send(handler(arr).encode())  # send back what the handler determines #
    # kept getting socket.error on terminating client so this is how I'm handling it #
    except error:  # catch socket.error and pass #
        connected(serverSocket)  # allows for the server to be reconnected after termination #

def main():
    # connect to client, taken from chapter 2 slides #
    serverPort = 12000
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print ("The server is ready to receive")
    connected(serverSocket)  # function to connect to client #


main()  # run the main function #
