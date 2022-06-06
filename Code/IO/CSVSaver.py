import csv
import os
from tkinter import filedialog
from tkinter.messagebox import showwarning
from Code.State import StateControl


def saveCSV(data):
    '''data is in the form [row1,row2...] where each row is an iterable
where each element can be converted into a string.
    '''
    filetypes = (('CSV files','*.csv'),)

    try:
        csvFileName = filedialog.asksaveasfilename(
            title='Save CSV',
            initialdir=os.getcwd(),
            filetypes=filetypes)

        csvFile = open(csvFileName,mode='w',newline='')
        writer = csv.writer(csvFile)
        for row in data:
            writer.writerow([str(value) for value in row])

        csvFile.close()
    except:
        showwarning(title='CSV Saver exception!',
                    message='There was an exception saving the requested CSV file.')
        csvFile.close()

def saveTimeSeriesData():
    saveCSV(StateControl.mainState.timeSeriesData)

#if I were being consistent I would also make saveCSV take a function argument
# but its not needed
