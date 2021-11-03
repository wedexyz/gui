import socket
import argparse
import json
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument("--ip",default="127.0.0.1", help="The ip to listen on")
parser.add_argument("--port",type=int, default=12346, help="The port to listen on")
parser.add_argument("--address",default="/openbci", help="address to listen to")
args = parser.parse_args()
# Connect to socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = (args.ip, args.port)
sock.bind(server_address)


def tes(data):
    do =[]
    for i in range (1) :
        for i in range (data):
          data, addr = sock.recvfrom(20000)
          obj = json.loads((data))
          dat = obj.get('data')
          dat = list(dat)
          do.append(dat)
    do = pd.DataFrame(do,columns=['ch1','ch2','ch3','ch4','ch5','ch6','ch7','ch8'])
    return do,dat
