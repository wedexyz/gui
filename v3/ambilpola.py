import socket
import json
import time
import numpy as np
import pandas as pd
from datetime import datetime
from playsound import playsound

from db import *

playsound('sound/testi.mp3')


now = datetime.now()
msgFromClient       = "200"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 5000)
bufferSize          = 20000
UDPClientSocket     = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

waktu =3
jumlah_data = 600


def mgg(jumlah_data):
    dat =[]

    for i in range(1):
        for i in range(jumlah_data):
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            dec = json.loads(msgFromServer[0].decode())
            a = dec.get("d1")
            b = dec.get("d2")
            c = dec.get("d3")
            d = dec.get("d4")
            e = dec.get("d5")
            f = dec.get("d6")
            g = dec.get("d7")
            h = dec.get("d8")
            x = a,b,c,d,e,f,g,h
            print(x)
            dat.append(x)

    dat = np.array(dat)
    df  = pd.DataFrame(dat)
    df.columns = ['data1','data2','data3','data4','data5','data6','data7','data8']
    df.insert(8,"label",1)

   

    return df

def st(jumlah_data):
    dat =[]
    for i in range(1):
        for i in range(jumlah_data):
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            dec = json.loads(msgFromServer[0].decode())
            a = dec.get("d1")
            b = dec.get("d2")
            c = dec.get("d3")
            d = dec.get("d4")
            e = dec.get("d5")
            f = dec.get("d6")
            g = dec.get("d7")
            h = dec.get("d8")
            x = a,b,c,d,e,f,g,h
            print(x)
            dat.append(x)

    dat = np.array(dat)
    df = pd.DataFrame(dat)
    df.columns = ['data1','data2','data3','data4','data5','data6','data7','data8']
    df.insert(8,"label",0)

    return df 

def mj(jumlah_data):
    dat =[]
    for i in range(1):
        for i in range(jumlah_data):
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            dec = json.loads(msgFromServer[0].decode())
            a = dec.get("d1")
            b = dec.get("d2")
            c = dec.get("d3")
            d = dec.get("d4")
            e = dec.get("d5")
            f = dec.get("d6")
            g = dec.get("d7")
            h = dec.get("d8")
            x = a,b,c,d,e,f,g,h
            print(x)
            dat.append(x)

    dat = np.array(dat)
    df = pd.DataFrame(dat)
    df.columns = ['data1','data2','data3','data4','data5','data6','data7','data8']

    df.insert(8,"label",2)
    return df 

for i in range (50):
  ct = pd.datetime.now().microsecond
 
  sm = st(jumlah_data)
  db.child("suara").set("0")
  sm.to_csv(f"st/{str(ct)}.csv")
  playsound('sound/tb.mp3')
 
  mt = mgg(jumlah_data)
  db.child("suara").set("1")
  mt.to_csv(f"mgg/{str(ct)}.csv")
  playsound('sound/tm.mp3')

  jp = mj(jumlah_data)
  db.child("suara").set("2")
  jp.to_csv(f"mj/{str(ct)}.csv")
  playsound('sound/tj.mp3')
  

 
   