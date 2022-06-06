import numpy
from scipy.signal import spectrogram

#window types
HANN = 'hann'

def generateSpectrogram(data,window=HANN,windowWidth=1.0,windowSpace=0.5):
    #Note: Data is in the csv loaded format [[x1,y1],[x2,y2]...]
    (timeData,ampData) = (d for d in data.T)

    #determine sampling rate, assuming constant
    sampleRate = 1/(timeData[1]-timeData[0])

    #number of datapoints per window:
    
    
    
    #generate hann windowing array

    #initialize spectrogram array
    
    #loop over data

        #convolve window and sliced data

        #do FFT

        #save to spectrogram

    #oooor just make the damn spectrogram with scipy
	#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.spectrogram.html
