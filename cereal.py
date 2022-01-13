# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 15:11:50 2021

@author: sbehje
"""

import serial

# USE WITH VIRTUAL ENVIRONMENT 'CENV'

# DON'T FORGET TO CLOSE SERIAL PORT W/ ser.close()
# CHECK SERIAL PORT OPEN/CLOSE STATE W/ ser.isOpen()

# Open Serial Port
ser = serial.Serial('COM8',
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1,
                    timeout=4,
                    xonxoff=False,
                    rtscts=False
                    )
# print(ser.name)          # print which port is used



# rawData  = ser.read()       # read serial data from USB->Serial device

while 1:
    # ser.write(b'hello00000')      # write a string
    # ser.write(b'world')      # write a string
    # ser.write(b'wheee')      # write a string
    # ser.write("1".encode())  # write an int
    rawData = ser.read()
    if rawData:
        print(rawData)
    
# ser.close()             # close port
