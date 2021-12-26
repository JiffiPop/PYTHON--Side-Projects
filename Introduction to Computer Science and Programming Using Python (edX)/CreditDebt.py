#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:05:12 2018

@author: jeff
"""
balance = 42 #amt NOT paid yet, amt due
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month=1
monthlyInterestRate = (annualInterestRate/12)
while month <= 12:
    minimumMonthlyPayment = (monthlyPaymentRate*balance)
    monthlyUnpaidBalance = (balance-minimumMonthlyPayment)
    updatedBalance = (monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance)
    balance = round(updatedBalance,2)
    month += 1
print("Remaining balance: " + str(balance))
