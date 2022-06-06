"""Utility functions and options for loading CSV files."""
import csv
import numpy
import os
from tkinter import filedialog
from tkinter.messagebox import showwarning
from Code.State import StateControl
from Code.UI import PlotUtils

def loadCSVData(dataStorageFunction):
    '''dataStorageFunction is a setter function that handles the loaded data
    '''
    #add confirmation popup
    
    filetypes = (('CSV files','*.csv'),)

    try:
        csvFile = filedialog.askopenfile(
            title='Open a file',
            initialdir=os.getcwd(),
            filetypes=filetypes)

        if not csvFile: return
        
        #parse file and save to data
        reader = csv.reader(csvFile)
        tempData = []
        for row in reader:
            #this is not safe
            tempData.append([float(element) for element in row])

        #only after read and parse is compelte without errors, store data
        dataStorageFunction(numpy.array(tempData))

        #and close file
        csvFile.close()
        
    except:# would be better to have specific exceptions
        showwarning(title='CSV Opener exception!',
                    message='There was an exception opening the requested CSV file.')
        csvFile.close()

def loadTimeSeriesData():
    loadCSVData(StateControl.mainState.setTimeSeriesData)
    StateControl.mainState.timePlot.update()
    #PlotUtils.updatePlot(StateControl.mainState.timePlot)
