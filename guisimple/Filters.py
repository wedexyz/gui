import socket
import argparse
import json
from numpy.core.numeric import True_
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fft import fft, fftfreq
import scipy.signal
from sklearn.preprocessing import StandardScaler

# konverter windowing
def window_data(df, window, feature_col_number, target_col_number):
    X = []
    y = []
    for i in range(len(df) - window - 1):
        features = df.iloc[i: (i+window), feature_col_number]
        target = df.iloc[(i + window), target_col_number]
        X.append(features)
        y.append(target)
    return np.array(X), np.array(y).astype(np.float64).reshape(-1, 1)

# Collect command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--ip",default="127.0.0.1", help="The ip to listen on")
parser.add_argument("--port",type=int, default=12347, help="The port to listen on")
parser.add_argument("--address",default="/openbci", help="address to listen to")
args = parser.parse_args()
# Connect to socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = (args.ip, args.port)
sock.bind(server_address)
# Receive messages
print("Listening...")
plt.style.use('dark_background')  
fig, axs = plt.subplots(1,2)
                   
def tes():
    do =[]
    for i in range (1) :
        for i in range (50):
          data, addr = sock.recvfrom(20000)
          obj = json.loads((data))
          print(obj)
          dat = obj.get('data')
          dat = list(dat)
          do.append(dat)
    do = pd.DataFrame(do,columns=['ch1','ch2','ch3','ch4','ch5','ch6','ch7','ch8'])
    window_size = 25
    (x, y) = window_data(do, window_size, 0, 0)
    y = pd.DataFrame(y)
    x = pd.DataFrame(x)
    #print(x.head())
    #print(y.head())

    #lo,hi=.07,.13
    #sr,y=do.ch1
    #b,a=signal.butter(N=3, Wn=[1*lo, 1*hi], btype='band')
    #b, a = scipy.signal.butter(  3, [.07, .13],'band')
    #b, a = scipy.signal.butter(  3,
                                # [.07, .13],
                                 #'band')

    b,a = signal.iirdesign( wp    = [0.07, 0.13],
                            #ws    = [0.06, 0.013], 
                            ws    = [0.01, 0.01],
                            gstop = 60, 
                            gpass = 1, 
                            ftype='ellip')

    filteredBandPass = scipy.signal.lfilter(b, a, do.ch1)
    print(filteredBandPass.shape)
    print(x.shape)
  
    axs[0].set_title('sinyal asli ')
    axs[0].plot(do.ch1)
    #axs[0].plot(x.loc[1])
    #axs[0].plot(x.loc[23])
    axs[1].set_title('Band Pass Filter')
    axs[1].plot(filteredBandPass )
    #axs[1].plot(a)
 
 
   
    fig.canvas.flush_events()
    axs[0].cla()
    axs[1].cla()
 

    
    
while True:
    tes()
    fig.canvas.manager.show() 
  




