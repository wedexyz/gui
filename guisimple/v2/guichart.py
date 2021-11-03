import PySimpleGUI as sg
from random import randint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from dataopbci import *
from fiter import *
import os
import joblib

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def main():
    layout =[ 
            
            [sg.Text('low', size=(5, 1),background_color='black')],

            [
            sg.Slider(range=(0, 20), default_value=0, size=(40, 10),orientation='h', key='-SLIDER-LOW-',background_color='black'),
            sg.Button('Exit', size=(10, 1), pad=((280, 0), 3), font='Helvetica 14'),
            ],  

            [sg.Text('high', size=(5, 1),background_color='black')],

            [
            sg.Slider(range=(1,50),   default_value=1,  size=(40, 10),orientation='h', key='-SLIDER-HIGH-',background_color='black'),
            sg.Button('rekam', size=(10, 1), pad=((280, 0), 3), font='Helvetica 14'),
            sg.Text('jumlah data', size=(5, 1),background_color='black'),
            sg.Input(key='-INPUT1-',size=(15, 10)),
            sg.Text('nama', size=(5, 1),background_color='black'),
            sg.Input(key='-INPUT2-',size=(15, 10)),
            ],

            [sg.Text('data',background_color='black')],

            [
            sg.Slider(range=(0, 250), default_value=50, size=(40, 10),orientation='h', key='-SLIDER-DATAPOINTS-',background_color='black'),
            sg.Text(size=(40,1), key='-OUTPUT-',background_color='black', pad=((280, 0), 3)),
             ],

            [sg.Canvas( key='-CANVAS-',size=(640, 480)),
           ],
      
            ]
   
    window = sg.Window('Demo Open BCi',layout, finalize=True,
    background_color='black',
    resizable=True,
    #no_titlebar=True, 
    location=(0,0), 
    size=(800,600), 
    keep_on_top=True
    ).finalize()
    canvas_elem = window['-CANVAS-']
    #window.Maximize()
    canvas = canvas_elem.TKCanvas
    plt.style.use('dark_background')
    fig, ax = plt.subplots(5, 1,  sharex=True)
    fig_agg = draw_figure(canvas, fig)

    NUM_DATAPOINTS = 1000
    dpts = [randint(0, 1) for x in range(NUM_DATAPOINTS)]
    for i in range(len(dpts)):
        event, values = window.read(timeout=5)
        
        ax[0].cla()                  
        ax[1].cla()
        ax[2].cla()
        ax[3].cla()
        ax[4].cla()

        ax[0].grid()                  
        ax[1].grid()
        ax[2].grid()
        ax[3].grid()
        ax[4].grid()
        

            
            
        
        data_points = int(values['-SLIDER-DATAPOINTS-']) 
        low  = int(values['-SLIDER-LOW-']) 
        high = int(values['-SLIDER-HIGH-']) 
        do,dat =tes(data_points)
        do = pd.DataFrame(do,columns=['ch1','ch2','ch3','ch4','ch5','ch6','ch7','ch8'])


        x1=filtered(low/100,high/100,do.ch1)
        x2=filtered(low/100,high/100,do.ch2)
        x3=filtered(low/100,high/100,do.ch3)
        x4=filtered(low/100,high/100,do.ch4)
        x5=filtered(low/100,high/100,do.ch5)
     

        ax[0].plot(range(data_points), x1,  color='blue')
        ax[1].plot(range(data_points), x2,  color ='brown')
        ax[2].plot(range(data_points), x3,  color='red')
        ax[3].plot(range(data_points), x4,  color='orange')
        ax[4].plot(range(data_points), x5,  color='green')

                
        if event in ('Exit', None):
            exit(69)
        if event in ('rekam', None):
            window['-OUTPUT-'].update(' data: ' + 
                                        values['-INPUT1-'] + 
                                      ' nama: ' + 
                                        values['-INPUT2-'] +
                                        ' filter low: '+
                                        str(values['-SLIDER-LOW-']) + 
                                        '  filter high: ' +
                                        str(values['-SLIDER-HIGH-'])  
                                        )
            data = values['-INPUT1-'], values['-INPUT2-'], values['-SLIDER-LOW-'],values['-SLIDER-HIGH-'],
            
            joblib.dump(data,'jumlah.pkl')
            os.startfile("pola.py")


        fig_agg.draw()
  
    window.close()


if __name__ == '__main__':
    main()
 