#!/usr/bin/env python

""" The entry point/main for the demo.
This module is executable in the right environment.
"""

import tkinter as tk
#from tkinter import ttk
#from Code.IO import CSVLoader
from Code.UI import MainWindow
#from Code.UI import PlotUtils

#initialize window
root = tk.Tk()
MainWindow.mainWindow.initializeMainWindow(root)
root.mainloop()
