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

application = Flask(__name__ ,
            static_url_path='', 
            static_folder='sumber',
          
            template_folder='template')

@application.route('/sumber/<path:path>')
def static_file(path):
    return application.send_static_file(path)


    

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
            a = dec.get("a")
            b = dec.get("b")
            c = dec.get("c")
            d = dec.get("d")
            e = dec.get("e")
            f = dec.get("f")
            g = dec.get("g")
            h = dec.get("h")
            

            json_data = json.dumps(
                #{'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': random.random() * 1000}
                {'time': datetime.now().strftime('%M:%S'), 
                'v1': a,'v2': b,'v3': c,'v4': d,
                'v5': e,'v6': f,'v7': g,'v8': h,
                })
            print(json_data)
            yield f"data:{json_data}\n\n"
            time.sleep(0.00005)

    return Response(generate_random_data(), mimetype='text/event-stream')



if __name__ == '__main__':
    port = 5000#+ random.randint(0, 999)
    url = "http://127.0.0.1:{0}/".format(port)
    threading.Timer(1.5, lambda: webbrowser.open(url) ).start()
    application.run(host='127.0.0.1',threaded=False)