# -*- coding: utf-8 -*-
"""
This application was created to allow for easier acquisition of the maximum
resistance, and thus, maximum temperature in the motor during burn in. It
also serves as a platform for automating other similar tasks with ease.

Created by Jeffrey A. Houston on July 27th, 2021

Last updated on October 19th, 2021
"""

# =============================================================================
# NOTE: To successfully launch the application, the user needs to install the 
# correct packages, and probably wants to do so in a virtual environment. 
# This is so  the base environment doesn't get messed up if the user installs 
# incorrect versions of packages that results in something not working.
# This would result in the user most likely needing to reinstall Anaconda.
# =============================================================================

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
# import PyQt5.QtCore as qtc
from datetime import datetime
# from scipy.signal import chirp, find_peaks, peak_widths
# import matplotlib as mpl
import math
import numpy as np
# import pandas as pd  # for importing data from .xlsx spreadsheet

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add title
        self.setWindowTitle("SCHNEEBERGER")
        self.resize(400, 100)
        
        # create labels
        fTemperatureLabel = qtw.QLabel("Fahrenheit Temperature   ")
        fTemperatureLabel.setFont(qtg.QFont('Helvetica', 14))
        
        cTemperatureLabel = qtw.QLabel("Celcius Temperature         ")
        cTemperatureLabel.setFont(qtg.QFont('Helvetica', 14))
        
        fTemperatureUnitsLabel = qtw.QLabel("°F")
        fTemperatureUnitsLabel.setFont(qtg.QFont('Helvetica', 14))
        
        cTemperatureUnitsLabel = qtw.QLabel("°C")
        cTemperatureUnitsLabel.setFont(qtg.QFont('Helvetica', 14))
        
        restistanceLabel = qtw.QLabel("Maximum Resistance        ")
        restistanceLabel.setFont(qtg.QFont('Helvetica', 14))
        
        resistanceUnitsLabel = qtw.QLabel("kΩ")
        resistanceUnitsLabel.setFont(qtg.QFont('Helvetica', 14))
        
        label = qtw.QLabel("SCHNEEBERGER's Temperature Calculator")
        label.setFont(qtg.QFont('Helvetica', 10))
        
        dateLabel = qtw.QLabel("Last Updated:  10/19/2021")
        dateLabel.setFont(qtg.QFont('Helvetica', 8))
        
        # textbox display results
        self.fTemperatureTextbox = qtw.QLineEdit(self)
        self.fTemperatureTextbox.setFont(qtg.QFont('Helvetica', 14))
        self.cTemperatureTextbox = qtw.QLineEdit(self)
        self.cTemperatureTextbox.setFont(qtg.QFont('Helvetica', 14))
        self.resistanceTextbox = qtw.QLineEdit(self)
        self.resistanceTextbox.setFont(qtg.QFont('Helvetica', 14))

        # upload button
        uploadButton = qtw.QPushButton("Upload")
        uploadButton.setFont(qtg.QFont('Helvetica', 12))
        uploadButton.clicked.connect(self.upload)
        
        # calculate button
        calculateButton = qtw.QPushButton("Calculate")
        calculateButton.setFont(qtg.QFont('Helvetica', 12))
        calculateButton.clicked.connect(self.calculate)
        
        # quit button
        quitButton = qtw.QPushButton("Quit")
        quitButton.setFont(qtg.QFont('Helvetica', 10))
        quitButton.clicked.connect(self.close)
        # quitButton.resize(10,10)
                
        # Layout
        layout = qtw.QVBoxLayout()
        
        sideBySideLayout = qtw.QHBoxLayout()
        sideBySideLayout.addWidget(fTemperatureLabel)
        sideBySideLayout.addWidget(self.fTemperatureTextbox)
        sideBySideLayout.addWidget(fTemperatureUnitsLabel)
        layout.addLayout(sideBySideLayout)
        
        sideBySideLayout = qtw.QHBoxLayout()
        sideBySideLayout.addWidget(cTemperatureLabel)
        sideBySideLayout.addWidget(self.cTemperatureTextbox)
        sideBySideLayout.addWidget(cTemperatureUnitsLabel)
        layout.addLayout(sideBySideLayout)
        
        sideBySideLayout = qtw.QHBoxLayout()
        sideBySideLayout.addWidget(restistanceLabel)
        sideBySideLayout.addWidget(self.resistanceTextbox)
        sideBySideLayout.addWidget(resistanceUnitsLabel)
        layout.addLayout(sideBySideLayout)
        
        sideBySideLayout = qtw.QHBoxLayout()
        sideBySideLayout.addWidget(calculateButton)
        sideBySideLayout.addWidget(uploadButton)
        layout.addLayout(sideBySideLayout)
        
        layout.addWidget(label)
        layout.addWidget(dateLabel)
        layout.addWidget(quitButton)
        
        self.setLayout(layout)

        self.show()
        
    def upload(self):
        print("\nUploading...")
        global filePath
        filename = qtw.QFileDialog.getOpenFileName(self, "Open File", "/home/", ("Text Files (*.txt)"));
        filePath = filename[0]
        
        if(filePath != ''):
            print("\nUpload Success!\n\nFilepath:  ", filePath, "\n")
        else:
            print("\nFile Upload Failed!  Please try again!\n")
            
    def calculate(self):
        print('\nRunning Program...\n')
        
        # import and format data to be usable
        filePath = "C:/Users/SBEHJE/Desktop/KLA Winn Calculator/AFTER TEMP 1 - Copy.txt"     # temporary filepath to be used during testing of application
        textFile = open(filePath, "r", encoding='utf-16 LE')
        data = textFile.read()
        data = data.replace('\t', ';')
        data = data.replace('\n', ';')
        data = data.split(';')
        
        headerRows = 1      # number of header lines (or lines to be ignored)
        length = math.floor(len(data)/3)
        global resistance 
        global time
        resistance = []
        time = []
        for i in range(3*headerRows,length):
            resistance.append(data[3*i+2])       # resistance [kOhms]
            time.append(data[3*i])               # time
        for i in range(0,len(resistance)):
            resistance[i] = resistance[i].replace('kΩ', '')
            resistance[i] = float(resistance[i])
            time[i] = datetime.strptime(time[i],'%d/%m/%Y %H:%M:%S')
            # time[i] = time[i].strftime('%H')        # reformat time variable
                
        # manually import data from the manufacturer's spreadsheet
        tempC = [-40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]
        tempF = [-40.0, -38.2, -36.4, -34.6, -32.8, -31.0, -29.2, -27.4, -25.6, -23.8, -22.0, -20.2, -18.4, -16.6, -14.8, -13.0, -11.2, -9.4, -7.6, -5.8, -4.0, -2.2, -0.4, 1.4, 3.2, 5.0, 6.8, 8.6, 10.4, 12.2, 14.0, 15.8, 17.6, 19.4, 21.2, 23.0, 24.8, 26.6, 28.4, 30.2, 32.0, 33.8, 35.6, 37.4, 39.2, 41.0, 42.8, 44.6, 46.4, 48.2, 50.0, 51.8, 53.6, 55.4, 57.2, 59.0, 60.8, 62.6, 64.4, 66.2, 68.0, 69.8, 71.6, 73.4, 75.2, 77.0, 78.8, 80.6, 82.4, 84.2, 86.0, 87.8, 89.6, 91.4, 93.2, 95.0, 96.8, 98.6, 100.4, 102.2, 104.0, 105.8, 107.6, 109.4, 111.2, 113.0, 114.8, 116.6, 118.4, 120.2, 122.0, 123.8, 125.6, 127.4, 129.2, 131.0, 132.8, 134.6, 136.4, 138.2, 140.0, 141.8, 143.6, 145.4, 147.2, 149.0, 150.8, 152.6, 154.4, 156.2, 158.0, 159.8, 161.6, 163.4, 165.2, 167.0, 168.8, 170.6, 172.4, 174.2, 176.0, 177.8, 179.6, 181.4, 183.2, 185.0, 186.8, 188.6, 190.4, 192.2, 194.0, 195.8, 197.6, 199.4, 201.2, 203.0, 204.8, 206.6, 208.4, 210.2, 212.0, 213.8, 215.6, 217.4, 219.2, 221.0, 222.8, 224.6, 226.4, 228.2, 230.0, 231.8, 233.6, 235.4, 237.2, 239.0, 240.8, 242.6, 244.4, 246.2, 248.0, 249.8, 251.6, 253.4, 255.2, 257.0, 258.8, 260.6, 262.4, 264.2, 266.0]
        baseResistance = [564, 569, 574, 580, 585, 591, 597, 602, 608, 614, 620, 626, 632, 638, 644, 651, 657, 663, 669, 676, 682, 688, 695, 701, 707, 714, 720, 726, 733, 739, 745, 752, 758, 765, 772, 779, 785, 792, 799, 806, 813, 820, 827, 834, 841, 848, 856, 863, 870, 878, 885, 892, 900, 907, 915, 923, 930, 938, 945, 953, 961, 969, 977, 984, 992, 1000, 1008, 1016, 1023, 1031, 1039, 1047, 1055, 1063, 1071, 1079, 1088, 1096, 1105, 1113, 1122, 1130, 1139, 1148, 1156, 1165, 1174, 1183, 1192, 1201, 1210, 1219, 1228, 1238, 1247, 1256, 1265, 1275, 1284, 1294, 1303, 1312, 1322, 1331, 1341, 1350, 1360, 1369, 1378, 1388, 1397, 1406, 1415, 1425, 1434, 1444, 1454, 1464, 1474, 1484, 1494, 1504, 1515, 1525, 1536, 1546, 1557, 1567, 1578, 1588, 1599, 1610, 1620, 1631, 1641, 1652, 1662, 1673, 1683, 1694, 1704, 1714, 1725, 1735, 1746, 1756, 1767, 1778, 1789, 1799, 1810, 1821, 1831, 1842, 1852, 1862, 1872, 1882, 1892, 1902, 1911, 1920, 1929, 1938, 1946, 1954, 1962, 1969, 1976, 1983, 1989]
        # convert from ohm to kohm
        for i in range(0,len(baseResistance)):
            baseResistance[i] = baseResistance[i]/1000
        
# =============================================================================
#         # replace all values above threshold with first value that is below threshold
#         threshold = max(baseResistance)
#         peaksIndex = []
#         for i in range(0,len(resistance)):
#             if resistance[i] <= threshold:
#                 defaultResistance = resistance[i]
#                 break
#         for i in range(0,len(resistance)):
#             if resistance[i] >= threshold:
#                 resistance[i] = defaultResistance
#                 peaksIndex.append(i)
# =============================================================================

        # manual override for time difference between all points
        deltaTimeSeconds = []
        for i in range(0,len(time)):
            deltaTimeSeconds.append(0.5)
        # calculate time difference between all points
# =============================================================================
#         deltaTimeSeconds = []
#         for i in range(1,len(time)):
#             deltaTime = time[i] - time[i-1]
#             temp = deltaTime.total_seconds()
#             deltaTimeSeconds.append(temp)
# =============================================================================
        

        # set threshold to highest value in lookup table provided by motor manufacturer
        threshold = max(baseResistance)     
        
        # find first value below threshold
        for i in range(0,len(resistance)):
            if resistance[i] <= threshold:
                defaultResistance = resistance[i]
                break
            
        # find all values above threshold
        peaksIndex = []
        for i in range(0,len(resistance)):
            if resistance[i] >= threshold:
                # resistance[i] = defaultResistance     # replace resistance above threshold with 'default' resistance
                peaksIndex.append(i)
        
        # define find 'islands' in an array  using https://www.geeksforgeeks.org/find-all-ranges-of-consecutive-numbers-from-array/
        def findIslands(a):
            N = len(a)
            length = 1
            list = []
            if (N == 0):    # if array is empty, return empty list
                return list
            
            for i in range(1, N + 1):  # sift thru array from beginning to end
                if (i == N or a[i] - a[i - 1] != 1):
                    if (length == 1):
                        list.append(a[i - length])
                    else:
                        temp = [a[i - length], a[i - 1]]
                        list.append(temp)
                    length = 1
                else:
                    length += 1
            return list
        
        # use findIslands function to define island locations in peaksIndex
        islands = findIslands(peaksIndex)
        
        # determine lengths of islands in peaksIndex
        islandLength = []
        for i in range(0,len(islands)):
            if type(islands[i]) == list:
                temp = islands[i][1] - islands[i][0] + 1
                islandLength.append(temp)
            elif type(islands[i]) == int:
                islandLength.append(1)
                 
        timeDiffThres = 10      # time (s) threshold for temperature increases to be considered real
        
        deltaTimeSecondsIslands = []
        for i in range(0,len(islandLength)):
            if islandLength[i] > 1:
                deltaTime = time[islands[i][1]] - time[islands[i][0]]
                temp = deltaTime.total_seconds()
                deltaTimeSecondsIslands.append(temp)
                if deltaTimeSecondsIslands[-1] >= timeDiffThres:
                    temp1 = np.array(resistance,dtype=object)
                    print('\nUh-oh...  check for system fire!  The maximum resistance that lasted',  deltaTimeSecondsIslands[i],'s is', max(temp1[islands[i][0]:islands[i][1]]), 'kΩ\n')
                else:
                    for j in range(islands[i][0],islands[i][1]):
                        resistance[j] = defaultResistance
            else: 
                resistance[islands[i]] = defaultResistance
            
        global maxResistance
        global maxIndex
        global maxTime
        
        maxResistance = max(resistance)
        maxIndex = resistance.index(maxResistance)
        maxTime = time[maxIndex]
        print(maxResistance, 'kΩ at', maxTime)
        
        tempC = np.asarray(tempC)
        tempF = np.asarray(tempF)
        baseResistance = np.asarray(baseResistance)
        baseResistance = baseResistance/1000
        maxResistance = np.asarray(maxResistance)
            
        tempIndex = np.argmin(abs(baseResistance - 1000*maxResistance))
        maxTempC = tempC[tempIndex]
        maxTempF = tempF[tempIndex]
        
        maxResistance = str("{:.3f}".format(maxResistance))
        maxTempC = str("{:.1f}".format(maxTempC))
        maxTempF = str("{:.1f}".format(maxTempF))
        
        self.fTemperatureTextbox.setText(str(maxTempF))
        self.cTemperatureTextbox.setText(str(maxTempC))
        self.resistanceTextbox.setText(str(maxResistance))
        
        # mpl.pyplot.plot(time, resistance)
    
        
#Run the app
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
