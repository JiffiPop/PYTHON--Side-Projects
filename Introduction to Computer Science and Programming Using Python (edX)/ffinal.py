# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
def polysum(n,s):
    '''
    Function will sum the area and the perimeter squared of the regular polygon,
    and return the sum rounded to 4 decimal places.
    '''
    
    area = (0.25*n*s**2)/(math.tan(math.pi/n))
    perimeter = n*s
    perimeter_sq = perimeter**2
    final = area + perimeter_sq
    ffinal = round(final,4)
    return ffinal