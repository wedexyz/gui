import PySimpleGUI as sg
import serial.tools.list_ports
import os
import joblib
import time


ports = serial.tools.list_ports.comports()
layout = [
    [sg.Text("apabila tidak ada di scrool silahkan input manual",key='-OUTPUT-',background_color='black'),
        sg.Button('cek port'),
       
        sg.Button('Quit')],
        [sg.Combo(['COM1', 'COM2','COM3','COM4','COM5'],enable_events=True, key='combo',size=(20,1)),
          sg.Button('save') ,sg.Button('start')],
          [sg.Input(key='-INPUT-',size=(22,1)),
          sg.Button('manual'),
        ],
         
         ]

window = sg.Window('Versi Betha komunikasi open bci', layout,background_color='black')


while True:
    event, values = window.read()
    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
  
    window['-OUTPUT-'].update(values['-INPUT-'] + "{}: {} [{}]".format(port, desc, hwid))

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    p = values['-INPUT-']
    c = values['combo']

    if event in ('start', None):
        combo = values['combo'] 
        os.startfile("guichart.py")

    if event in ('save', None):
        joblib.dump(c,'hub.pkl')

    if event in ('manual', None):
        joblib.dump(p,'hub.pkl')


window.close()