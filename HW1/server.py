#Nick Majkic
#CSDS 325
from socket import *


store_inventory={}


def get(key):
    if key in store_inventory:
        return store_inventory[key]
    else:
        return "Cannot find \"" + key + "\" in the data store."


def put(key,value):
    if not isinstance(value,int):
        return "Value \"" + value + "\" is not valid."
    else:
        store_inventory[key]=value
        return "Successfully mapped \""+ value + "\" to \"" + key + "\"."


def mappings():
    output=""
    for key in list(store_inventory):
        output+= key + " " + store_inventory[key] + "\n"
    return output


def keyset():
    output=""
    for key in list(store_inventory):
        output+=key + "\n"
    return output


def values():
    output = ""
    for key in list(store_inventory):
        output += store_inventory[key] + "\n"
    return output


def main():
    serverPort = 12000
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print ("The server is ready to receive")
    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.
        encode())
        connectionSocket.close()