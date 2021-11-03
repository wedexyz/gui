import socket
import argparse
import json
import pandas as pd
from fiter import *
import joblib

import time
parser = argparse.ArgumentParser()
parser.add_argument("--ip",default="127.0.0.1", help="The ip to listen on")
parser.add_argument("--port",type=int, default=12345, help="The port to listen on")
parser.add_argument("--address",default="/openbci", help="address to listen to")
args  = parser.parse_args()
sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = (args.ip, args.port)
sock.bind(server_address)


load = joblib.load('jumlah.pkl')

jumlah_data = int(load[0])
nama        = (load[1])
low         = int(load[2])
high        = int(load[3])

print(load)
time.sleep(2)
def tes(jumlah_data):
    ch = []
    for i in range (1) :
        for i in range (jumlah_data):
            data, addr = sock.recvfrom(20000)
            obj = json.loads((data))
            dat = obj.get('data')
            dat = list(dat)
            print(dat)
            ch.append(dat)
    do = pd.DataFrame(ch,columns=['ch1','ch2','ch3',
                                        'ch4','ch5','ch6','ch7','ch8'])
    x1=filtered(low/100,high/100,do.ch1)
    x2=filtered(low/100,high/100,do.ch2)
    x3=filtered(low/100,high/100,do.ch3)
    x4=filtered(low/100,high/100,do.ch4)
    x5=filtered(low/100,high/100,do.ch5)
    
    x1 = pd.DataFrame(x1)
    x2 = pd.DataFrame(x2)
    x3 = pd.DataFrame(x3)
    x4 = pd.DataFrame(x4)
    x5 = pd.DataFrame(x5)
    


    datacap=pd.concat([x1,x2,x3,x4,x5],axis=1)
    datacap.columns =['c1','c2','c3','c4','c5']
    print(datacap)

    return datacap

#configurasi
#jumlah_data = 500 
nama_data = str(nama)
data_save = tes(jumlah_data)

data_save.to_csv(nama_data+ '.csv')
#print(data_save)

  




