#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 13:07:46 2018

@author: jeff
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    values = aDict.values()
    keysList = []
    if target in values:
        for i in aDict.keys():
            if aDict[i] == target:
                keysList.append(i)
                keysList.sort()
        return keysList
    else:
        return []