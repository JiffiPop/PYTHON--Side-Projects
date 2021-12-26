#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 13:07:46 2018

@author: jeff
"""
listA = [1, 2, 3]
listB = [4, 5, 6]

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    step1 = [listA[i] * listB[i] for i in range(len(listA))]
    step2 = sum(step1)
    return step2
