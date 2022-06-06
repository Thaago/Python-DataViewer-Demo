#import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import numpy as np

from scipy.signal import spectrogram as sg
from Code.State import StateControl
from Code.UI import MainWindow

import numpy

import matplotlib.style as mplstyle
mplstyle.use('fast')#Note: this is active code and must og after other styles

class PlotContainer():
    #container object with references for handling plots
    def __init__(self):
        self.axes = None
        self.canvas = None
        self.fig = None
        self.toolbar = None
        self.xData = None
        self.yData = None

    def update(self):
        self.axes.clear()
        self.axes.plot(self.xData,self.yData)
        #sets axes zoom, currently at max of data range, could use some padding
        self.axes.set_xlim([numpy.amin(self.xData),numpy.amax(self.xData)])
        self.axes.set_ylim([numpy.amin(self.yData),numpy.amax(self.yData)])
        self.toolbar.update()
        self.canvas.draw()

class SpecPlotContainer(PlotContainer):
    #container specifically for spectrograms with different update
    def __init__(self):
        super().__init__()
        self.rate = None
        self.cb = None

    def update(self):
        self.axes.clear()
        #average channel data for now, if more than 1 channel:
        if len(self.yData.shape)==1:
            data = self.yData
        elif len(self.yData.shape)==2:
            data = np.sum(self.yData,axis=1)/self.yData.shape[1]
        else:
            raise Exception("Spec data shape higher than 2 dimensions.")

        #create spectrogram, axis, title, and scale
        #segments are .1 seconds, overlap is that/8
        #there is a tradeoff between frequency precision and time precision
        #fundamental law of signal analysis
        #so a longer segment gives better freq, poor time, and vice versa
        #making this user adjustable with a slider would be nice
        f, t, Sxx = sg(data,self.rate,window=('hann'),nperseg =int(self.rate/10),
                       scaling='spectrum')
        Sxx = np.log(Sxx+1)#convert to log greater than 0
        im = self.axes.pcolormesh(t, f, Sxx, shading='gouraud')

        #self.axes.ylabel('Frequency [Hz]')
        #self.axes.xlabel('Time [sec]')
        if self.cb: self.cb.remove()
        self.cb = self.fig.colorbar(im, ax=self.axes)
        self.axes.set_title('Levels')

        self.toolbar.update()

        self.canvas.draw()

def createPlot(frame,container):
    # the figure that will contain the plot
    container.fig = Figure(figsize = (5, 5),
                 dpi = 100)
  
    # adding the subplot
    container.axes = container.fig.add_subplot(111)
  
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    container.canvas = FigureCanvasTkAgg(container.fig,master = frame)  
    container.canvas.draw()
  
    # placing the canvas on the Tkinter window
    container.canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    container.toolbar = NavigationToolbar2Tk(container.canvas,frame)
    container.toolbar.update()
  
    # placing the toolbar on the Tkinter window
    container.canvas.get_tk_widget().pack()

               
def createSpecButtonCallbackGenerator(container):
    def callback():
        container.update()
        
    return callback
