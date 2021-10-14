# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 12:55:28 2021

@author: sbehje
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math
from datetime import datetime
import scipy.signal


print('\nRunning Program...\n')
        
    # import and format data to be usable
filePath = "F:\Systems\Production\ATP_Forms\ATP 800 000 037 (565 400 192)\93\AFTER TEMP1.txt"
textFile = open(filePath, "r", encoding='utf-16 LE')
data = textFile.read()
data = data.replace('\t', ';')
data = data.replace('\n', ';')
data = data.split(';')

global resistance 
global time
index = []
resistance = []
time = []
headerRows = 1      # number of header lines (or lines to be ignored)
length = math.floor(len(data)/3)
for i in range(3*headerRows,length):
    index.append(i)
    resistance.append(data[3*i+2])       # resistance [kOhms]
    time.append(data[3*i])               # time
for i in range(0,len(resistance)):
    resistance[i] = resistance[i].replace('kΩ', '')
    resistance[i] = float(resistance[i])
    time[i] = datetime.strptime(time[i],'%d/%m/%Y %H:%M:%S')
    
# replace all values above threshold with first value that is below threshold
# =============================================================================
# threshold = 1.9
# for i in range(0,len(resistance)):
#     if resistance[i] <= threshold:
#         defaultResistance = resistance[i]
#         break
# for i in range(0,len(resistance)):
#     if resistance[i] >= threshold:
#         resistance[i] = defaultResistance
# =============================================================================

fig,ax1 = plt.subplots()
plt.plot(time,resistance)
monthyearFmt = mdates.DateFormatter('%X')
ax1.xaxis.set_major_formatter(monthyearFmt)
_ = plt.xticks(rotation=90)
plt.rcParams['figure.dpi'] = 300

# =============================================================================
# index, peaks = scipy.signal.find_peaks(resistance, height=1.1, threshold=None, distance=None, prominence=None, width=1, wlen=None, rel_height=0.5, plateau_size=None)
# print(index)
# print(peaks)
# =============================================================================

