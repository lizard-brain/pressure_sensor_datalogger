# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:54:29 2021

@author: jason

https://stackoverflow.com/questions/45046239/python-realtime-plot-using-pyqtgraph

kinda rough
"""


# Import libraries
from numpy import *
import pandas as pd
import numpy as np
import random
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

import csv
import time




# Import Data

file_name = 'file_name'

data_csv = './data/' + file_name + '.csv'

df_data = pd.read_csv(data_csv, skiprows=3)     # import DF

df_data.columns =['Time','Value']               # Name colums  
df_data = df_data.dropna()

print(df_data)

print(df_data.iat[0,1])

#from random import randrange, uniform


### START QtApp #####
app = QtGui.QApplication([])            # you MUST do this once (initialize things)

## Switch to using white background and black foreground
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


####################

win = pg.GraphicsWindow(title="Signal from serial port") # creates a window
#p = win.addPlot(title="INTENSITY")  # creates empty space for the plot in the window
p = win.addPlot()  # creates empty space for the plot in the window

p.setYRange(350,600, padding=0)           #     Set static Y scale
curve = p.plot(pen=pg.mkPen('r', width=4))                        # create an empty "plot" (a curve to plot)

windowWidth = 500                       # width of the window displaying the curve
Xm = linspace(0,0,windowWidth)          # create array that will contain the relevant time series     
ptr = -windowWidth                      # set first x position


#delta = 0
#value_raw = 0
value = 0
x = np.linspace(1, 10)
# Realtime data plot. Each time this function is called, the data display is updated

row_int = 0

def update():
    global curve, ptr, Xm, value
    global row_int    
    Xm[:-1] = Xm[1:]                      # shift data in the temporal mean 1 sample left
    
    
    #TESTER CODE
    
    
    
    value_raw = df_data.iat[row_int,1]           # READ DATA FROM DataFrame, counts up
    row_int = row_int + 1
    print(df_data.iat[row_int,0])
    value_raw = int(value_raw)
    
    time.sleep(0.0001)
    #value_raw = random.uniform(150, 250)#TEST CODE
    

    
    
    delta =  value_raw - value 
    delta = abs(delta)
    
    if delta > 3:
        value = value_raw
    #value = uniform(0, 10) TEST CODE
    
    
    Xm[-1] = float(value)                 # vector containing the instantaneous values      
    ptr += 1                              # update x position for displaying the curve
    curve.setData(Xm)                     # set the curve with this data
    curve.setPos(ptr,0)                   # set x position in the graph to 0
    QtGui.QApplication.processEvents()    # you MUST process the plot now
    
    
    

### MAIN PROGRAM #####    
# this is a brutal infinite loop calling your realtime data plot
while True: update()

### END QtApp ####
pg.QtGui.QApplication.exec_() # you MUST put this at the end
##################
