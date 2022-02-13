#Nick Majkic
#CSDS 325
from socket import *


store_inventory={}


def get(key):
    if key in store_inventory:
        return str(store_inventory[key])
    else:
        return "Cannot find \"" + key + "\" in the data store."


def put(key,value):
    if not isinstance(value,int):
        return "Value \"" + value + "\" is not valid."
    else:
        store_inventory[key]=value
        return "Successfully mapped \""+ str(value) + "\" to \"" + key + "\"."


def mappings():
    output=""
    for key in list(store_inventory):
        output+= key + " " + str(store_inventory[key]) + "\n"
    return output


def keyset():
    output=""
    for key in list(store_inventory):
        output+=key + "\n"
    return output


def values():
    output = ""
    for key in list(store_inventory):
        output += str(store_inventory[key]) + "\n"
    return output


def handler(arr):
    if len(arr)==3:
        if arr[0].lower() == "put":
            return put(arr[1], int(arr[2]))
    elif len(arr)==2:
        if arr[0].lower() == "get":
            return get(arr[1])
    elif len(arr)==1:
        if arr[0].lower() == "values":
            return values()
        elif arr[0].lower() == "keyset":
            return keyset()
        elif arr[0].lower() == "mappings":
            return mappings()
    return "Invalid command"


def main():
    serverPort = 12000
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print ("The server is ready to receive")
    connectionSocket, addr = serverSocket.accept()
    while True:
        sentence = connectionSocket.recv(1024).decode()
        print("Recieved: " + sentence)
        arr=sentence.split()
        if arr[0] =="bye":
            connectionSocket.close();
        connectionSocket.send(handler(arr).encode())

main()