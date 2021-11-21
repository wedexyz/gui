from pyOpenBCI import OpenBCICyton
import socket
import json
import pandas as pd
import joblib

localIP     = "127.0.0.1"
localPort   = 5000
bufferSize  = 1024
msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)
usb = joblib.load('port.pkl')
print(usb)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

def print_raw(sample):
    data = sample.channels_data
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    #message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    d1 = data[0]
    d2 = data[1]
    d3 = data[2]
    d4 = data[3]
    d5 = data[4]
    d6 = data[5]
    d7 = data[6]
    d8 = data[7]
    send = json.dumps({"d1": d1, "d2": d2,"d3":d3,"d4":d4 ,"d5":d5,
                        "d6":d6,"d7": d7,"d8":d8
    })
    datasend = str.encode(send)
    UDPServerSocket.sendto(datasend, address)
    print(datasend)

board = OpenBCICyton(port=usb, daisy=False)
board.start_stream(print_raw)




