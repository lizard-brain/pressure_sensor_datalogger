# -*- coding: utf-8 -*-
"""
Created on Sat May 22 18:26:56 2021

@author: Jason

cleans the dirty data from the dodgy serial reader
"""

import pandas as pd
from datetime import datetime
import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np

#csv_run cleans up the data and merges it into a single CSV


print('CSV Cleanup')    

# Import

# data  temp df

file_name = 'testdata'

data_csv = './data/' + file_name + '.csv'

df_data = pd.read_csv(data_csv, skiprows=3)     # import DF

df_data.columns =['Time','Value']               # Name colums  


print(df_data)

# Display Graph

'''
Need to read the Value colum and print the next value down, can just step it by a known interval

'''

fig = plt.figure()

def buildmebarchart(i=int):
    p = plt.plot(df_data[0].index,df_data[0].values,)
    
    
animator = ani.FuncAnimation(fig, buildmebarchart, interval = 100)

plt.show()
print('go')