# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:54:29 2021

@author: jason

https://stackoverflow.com/questions/45046239/python-realtime-plot-using-pyqtgraph

super rushed - kinda janky but works
"""


# Import libraries
from numpy import *
import numpy as np
import random
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import serial
import csv
import time

# Create object serial port
portName = "COM5"                      # replace this port name by yours!

baudrate = 9600



#No serial example


ser = serial.Serial(portName,baudrate)

#from random import randrange, uniform


### START QtApp #####
app = QtGui.QApplication([])            # you MUST do this once (initialize things)
####################

win = pg.GraphicsWindow(title="Signal from serial port") # creates a window
#p = win.addPlot(title="INTENSITY")  # creates empty space for the plot in the window
p = win.addPlot()  # creates empty space for the plot in the window

p.setYRange(300,600, padding=0)           #     Set static Y scale
curve = p.plot(pen=pg.mkPen('r', width=2))                        # create an empty "plot" (a curve to plot)

windowWidth = 500                       # width of the window displaying the curve
Xm = linspace(0,0,windowWidth)          # create array that will contain the relevant time series     
ptr = -windowWidth                      # set first x position


#delta = 0
#value_raw = 0
value = 0
x = np.linspace(1, 10)
# Realtime data plot. Each time this function is called, the data display is updated
def update():
    global curve, ptr, Xm, value    
    Xm[:-1] = Xm[1:]                      # shift data in the temporal mean 1 sample left
    
    
    #TESTER CODE
    value_raw = ser.readline()                # read line (single value) from the serial port
    value_raw = int(value_raw)
    
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
    
    
    #CSV Writter Hacky af
    #decoded_bytes = float(value[0:len(value)-2].decode("utf-8")) cuze its already being filtered
    #print(decoded_bytes)
    with open("test_data.csv","a") as f:
        writer = csv.writer(f,delimiter=",")
        writer.writerow([time.time(),value])
    
    

### MAIN PROGRAM #####    
# this is a brutal infinite loop calling your realtime data plot
while True: update()

### END QtApp ####
pg.QtGui.QApplication.exec_() # you MUST put this at the end
##################
