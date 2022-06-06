"""Holds information and functions for accessing and changing the program state."""
import numpy
from Code.IO import WAVUtils
from Code.UI import PlotUtils

class ProgramState():
    '''Data container class for the program state.
    '''
    def __init__(self):
        self.timeSeriesData = numpy.array([])# in csv format
        self.timeSeriesX = []
        self.timeSeriesY = []
        self.psdData = numpy.array([])
        self.activeFilters = numpy.array([])
        self.wavContainer = WAVUtils.WavContainer()
        self.timePlot = PlotUtils.PlotContainer()
        self.specPlot = PlotUtils.SpecPlotContainer()

    def setTimeSeriesData(self,data):
        #its weird to need a setter in python, but its the cleanest
        # way to have a function based CSV loader
        self.timeSeriesData = numpy.array(data)
        self.timeSeriesX = self.timeSeriesData.T[0]
        self.timeSeriesY = self.timeSeriesData.T[1]
        #self.timePlot = numpy.array(data)
        self.timePlot.xData = self.timeSeriesData.T[0]
        self.timePlot.yData = self.timeSeriesData.T[1]

    
        

#The default program state object, accessible to other modules via StateControl.mainState
mainState = ProgramState()


def swapMainState(newState):
    '''Unimplemented: the required steps needed to completely swap the
program state and update all dependent visuals etc.
    '''
    pass
