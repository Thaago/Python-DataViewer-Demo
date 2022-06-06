import tkinter as tk
from tkinter import ttk
from Code.IO import CSVLoader, CSVSaver, WAVUtils
from Code.UI import PlotUtils
from Code.State import StateControl

class MainWindow():
    def __init__(self):
        self.root = None
        self.title = "Data Viewer Demo"
        self.width = 1200
        self.height = 800
        self.resize = True
        
    def initializeMainWindow(self,root):
        self.root = root#needs to be the actual root of the tk application for quit to work
        self.root.title(self.title)
        self.root.resizable(self.resize,self.resize)
        self.root.geometry(str(self.width)+'x'+str(self.height))

        self.baseFrame = tk.Frame(self.root)
        self.baseFrame.pack()

        #add loading button
        self.buttonFrame = tk.Frame(self.baseFrame)
        self.buttonFrame.pack(side=tk.TOP)
        self.loadCSVButton = ttk.Button(self.buttonFrame, text='Load CSV Data',command=CSVLoader.loadTimeSeriesData)
        self.loadCSVButton.pack(side=tk.LEFT)

        #save button
        self.saveCSVButton = ttk.Button(self.buttonFrame, text='Save CSV Data',command=CSVSaver.saveTimeSeriesData)
        self.saveCSVButton.pack(side=tk.LEFT)

        #quit button:
        self.quitButton = ttk.Button(self.buttonFrame, text="Quit", command=self.pQuit)
        self.quitButton.pack(side=tk.RIGHT)

        #wavopen button
        self.loadWavButton = ttk.Button(self.buttonFrame, text="Load WAV",
                                        command=WAVUtils.loadWavButtonCallbackGenerator(
                                            StateControl.mainState.wavContainer))
        self.loadWavButton.pack(side=tk.LEFT)

        #wavplay button
        self.wavPlayButton = ttk.Button(self.buttonFrame, text="Play WAV",
                                        command=WAVUtils.playWavButtonCallbackGenerator(
                                            StateControl.mainState.wavContainer))
        self.wavPlayButton.pack(side=tk.LEFT)

        # Frame for graphics:
        self.plotFrames = tk.Frame(self.baseFrame)
        self.plotFrames.pack(side=tk.BOTTOM)
        #time series plot
        self.timeSeriesFrame = tk.Frame(self.plotFrames)
        #self.timeSeriesFig,self.timeSeriesAxes,self.timeSeriesCanvas = PlotUtils.createPlot(self.timeSeriesFrame,[0],[0])
        PlotUtils.createPlot(self.timeSeriesFrame,StateControl.mainState.timePlot)
        self.timeSeriesFrame.pack(side=tk.LEFT)

        #spectrogram plot
        
        self.spectrogramFrame = tk.Frame(self.plotFrames)
        #self.spectrogramFig,self.spectrogramAxes,self.spectrogramCanvas = PlotUtils.createPlot(self.spectrogramFrame,[0],[0])
        PlotUtils.createPlot(self.spectrogramFrame,StateControl.mainState.specPlot)
        self.spectrogramFrame.pack(side=tk.RIGHT)
    
    def pQuit(self):
        self.root.quit()     
        self.root.destroy()

#the default main window object, accessible to other modules via MainWindow.mainWindow
mainWindow = MainWindow()
