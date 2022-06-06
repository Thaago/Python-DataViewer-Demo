import numpy as np
import scipy.io.wavfile as wf
import simpleaudio as sa
from tkinter import filedialog
from tkinter.messagebox import showwarning
import traceback
import os
from Code.State import StateControl

#notes: sample rate is usually 44100
#bytes per sample is usually 2? But scipy's read will automatically set it

class WavContainer():
    #container object with data for wav files
    def __init__(self):
        self.wavData = None
        self.rate = None
        self.bytesPerSample = None
        self.numChannels = None

def loadWavButtonCallbackGenerator(container,plot=True):
    #container requires a rate, wavData,bytesPerSample,numChannels field
    def callback():
        try:
            #open a dialog
            wavFile = filedialog.askopenfilename(
                title='Select wav file to open',
                initialdir=os.getcwd(),
                filetypes=(('wav files','*.wav'),))

            if not wavFile: return

            #read the data
            container.rate,container.wavData = wf.read(wavFile)
            #check and save the bytes per sample
            dType = container.wavData.dtype
            if dType==np.float32 or dType==np.int32:
                container.bytesPerSample=4
            elif dType==np.int16:
                container.bytesPerSample=2
            elif dType==np.uint8:
                container.bytesPerSample=1
            else:
                raise Exception("wav import dType not recognized")
            #check and save channel number
            container.numChannels = len(container.wavData.shape)
            
            
            #wavFile.close()
        except:
            showwarning(title='Wav Loader exception!',
                    message=traceback.print_exc())
            #wavFile.close()

        if plot:
            #if this is true, then it plots the series and spectrogram
            #set time series data
            StateControl.mainState.timePlot.yData = container.wavData
            StateControl.mainState.timePlot.xData = np.arange(
                len(StateControl.mainState.timePlot.yData))/container.rate
            #update time series plot
            StateControl.mainState.timePlot.update()

            #set the spectrogam data
            StateControl.mainState.specPlot.yData = container.wavData
            StateControl.mainState.specPlot.rate = container.rate
            StateControl.mainState.specPlot.update()
        
    return callback

def saveWavButtonCallbackGenerator(container):
    #container requires a rate and wavData field
    def callback():
        try:
            wavFile = filedialog.asksaveasfilename(
                title='Select wav file to write',
                initialdir=os.getcwd(),
                filetypes=(('wav files','*.wav'),))
            
            wf.write(wavFile,container.rate,container.wavData)
            #wavFile.close()
        except:
            showwarning(title='Wav Saver exception!',
                    message=traceback.print_exc())
            #wavFile.close()
        
    return callback

def playWavButtonCallbackGenerator(container):
    #container requires a wavData, rate, numChannels,bytesPerSample field
    def callback():
        sa.play_buffer(container.wavData,container.numChannels,
                       container.bytesPerSample,container.rate)

    return callback
        
