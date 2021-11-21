from flask import Flask, render_template, url_for, request
import random, threading, webbrowser
import serial.tools.list_ports
import joblib
import os


#for hub, desc, hwid in sorted(ports):
        #print("{}: {} [{}]".format(hub, desc, hwid))


application = Flask(__name__ ,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@application.route('/static/<path:path>')
def static_file(path):
    return application.send_static_file(path)

@application.route('/',methods=['GET','POST'])
def index():
    ports = serial.tools.list_ports.comports()
    for hub, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(hub, desc, hwid))
    if request.method=='POST':
        nama = request.form['nama']
       
        joblib.dump(nama,'port.pkl')
        print(nama)
        os.startfile("server.py")
        os.startfile("interface.py")
    return render_template('awal.html', variable= hub)


if __name__ == '__main__':
    port = 8000#+ random.randint(0, 999)
    url = "http://127.0.0.1:{0}/".format(port)
    threading.Timer(1.5, lambda: webbrowser.open(url) ).start()
    application.run(host='127.0.0.1',threaded=False,port=8000)