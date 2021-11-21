import os
import sys
import socket
import random
import json

localIP     = '127.0.0.1'
localPort   =5000


bufferSize  = 20000

UDPServerSocket     = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

def dataen():
    d1 = random.randint(0,5)
    d2 = random.randint(5,10)
    d3 = random.randint(10,15)
    d4 = random.randint(15,20)

    d5 = random.randint(20,25)
    d6 = random.randint(25,30)
    d7 = random.randint(30,35)
    d8 = random.randint(35,40)

    data = json.dumps({"a": d1, "b": d2, "c": d3,"d": d4,
                          "e": d5, "f": d6 ,"g": d7, "h": d8
                        })
    data = str.encode(data)
    print(data)
    return data


while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    data = dataen()
    UDPServerSocket.sendto(data, address)