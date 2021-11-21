import json
import random
import time
from datetime import datetime
import random, threading, webbrowser
import socket

from flask import Flask, Response, render_template
from flask import Flask, request
application = Flask(__name__)
random.seed()  # Initialize the random number generator
msgFromClient       = "200"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 5000)
bufferSize          = 20000
UDPClientSocket     = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

@application.route('/')
def index():
    return render_template('index.html')


@application.route('/chart-data')
def chart_data():
    def generate_random_data():
        while True:
            
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
            

            json_data = json.dumps(
                #{'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': random.random() * 1000}
                {'time': datetime.now().strftime('%M:%S'), 
                'v1': a,'v2': b,'v3': c,'v4': d,
                'v5': e,'v6': f,'v7': g,'v8': h,
                }

                )
            print(json_data)
            yield f"data:{json_data}\n\n"
            time.sleep(0.09)

    return Response(generate_random_data(), mimetype='text/event-stream')



if __name__ == '__main__':
    port = 5000#+ random.randint(0, 999)
    url = "http://127.0.0.1:{0}/".format(port)
    threading.Timer(1.5, lambda: webbrowser.open(url) ).start()
    application.run(host='127.0.0.1',threaded=False)