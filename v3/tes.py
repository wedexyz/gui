import socket
import json

import numpy as np
import pandas as pd
from datetime import datetime
from playsound import playsound

import joblib
from db import *
model = joblib.load('mem4.pkl')

playsound('sound \\selamat datang dipercobaan betha tess EEG .mp3')
now = datetime.now()
msgFromClient       = "200"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 5000)
bufferSize          = 20000
UDPClientSocket     = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


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
            #print(x)
            dat.append(x)

    dat = np.array(dat)
    df = pd.DataFrame(dat)
    df.columns = ['data1','data2','data3','data4','data5','data6','data7','data8']

   

    return df
while True :
  mt = mgg(jumlah_data)
  print(model.predict(mt)[0])
  out = model.predict(mt)[0]
  if out == 0 :
      print("idle")
      db.child("suara").set("0")
      playsound('sound \\tangan membuka (1).mp3')
  elif out ==1 :
        print("mengengam")
        db.child("suara").set("1")
        playsound('sound \\tangan menggenggam (1).mp3')
  elif out ==2 :
        print('menjimpit')
        db.child("suara").set("2")
        playsound('sound \\tangan menjimpit.mp3')





 
   