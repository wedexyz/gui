import PySimpleGUI as sg
from random import randint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
# Yet another usage of MatPlotLib with animations.

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def main():

    NUM_DATAPOINTS = 1000
    # define the form layout
    #layout = [[sg.Text('Animated Matplotlib', size=(40, 1),
               # justification='center', font='Helvetica 20')],
                
    layout =[[sg.Canvas(size=(640, 480), key='-CANVAS-')],
            [sg.Text('Progress through the data')],
              [sg.Slider(range=(0, NUM_DATAPOINTS), size=(60, 10),
                orientation='h', key='-SLIDER-')],
              [sg.Text('Number of data points to display on screen')],
              [sg.Slider(range=(10, 500), default_value=40, size=(40, 10),
                    orientation='h', key='-SLIDER-DATAPOINTS-')],
              [sg.Button('Exit', size=(10, 1), pad=((280, 0), 3), font='Helvetica 14')]]

    # create the form and show it without the plot
    window = sg.Window('Demo Open BCi',layout, finalize=True)
    canvas_elem = window['-CANVAS-']
    slider_elem = window['-SLIDER-']
    canvas = canvas_elem.TKCanvas

    # draw the initial plot in the window
    fig, ax = plt.subplots(5, 1,  sharey=True,sharex=True)
    #fig = Figure()

    #ax = fig.add_subplot(111)
    ax[0].set_xlabel("X axis")
    ax[0].set_ylabel("Y axis")
    ax[0].grid()
    fig_agg = draw_figure(canvas, fig)
    # make a bunch of random data points
    dpts = [randint(0, 10) for x in range(NUM_DATAPOINTS)]
    
    for i in range(len(dpts)):
    #while True :

        event, values = window.read(timeout=10)
        if event in ('Exit', None):
            exit(69)
        #slider_elem.update(i)       # slider shows "progress" through the data points
        ax[0].cla()                    # clear the subplot
        ax[1].cla()
        ax[2].cla()
        ax[3].cla()
        ax[4].cla()


        ax[0].grid()                   # draw the grid
        ax[1].grid()
        ax[2].grid()
        ax[3].grid()
        ax[4].grid()

        data_points = int(values['-SLIDER-DATAPOINTS-']) # draw this many data points (on next line)
        
        
        ax[0].plot(range(data_points), dpts[i:i+data_points],  color='purple')
        ax[1].plot(range(data_points), dpts[i:i+data_points],  color='blue')
        ax[2].plot(range(data_points), dpts[i:i+data_points],  color='red')
        ax[3].plot(range(data_points), dpts[i:i+data_points],  color='yellow')
        ax[4].plot(range(data_points), dpts[i:i+data_points],  color='green')

        x = np.array(dpts[i:i+data_points])


        print(x.shape)
        fig_agg.draw()

    window.close()

if __name__ == '__main__':
    main()