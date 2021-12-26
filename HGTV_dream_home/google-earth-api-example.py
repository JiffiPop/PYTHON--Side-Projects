#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 11:33:27 2021

@author: jeff
"""

# this file simply follows the example written here:
    # https://github.com/google/earthengine-community/blob/master/tutorials/intro-to-python-api-guiattard/index.ipynb



import ee
import geemap

Map = geemap.Map()

Map

landcover = ee.Image('USGS/NLCD/NLCD2016').select('landcover')
Map.addLayer(landcover, {}, 'Landcover Map 2016')


# =============================================================================
# import ee    # pip install earthengine-api --upgrade
# ee.Authenticate()   # trigger authentication flow
# ee.Initialize()     # initialize library
# 
# # Import the MODIS land cover collection.
# lc = ee.ImageCollection('MODIS/006/MCD12Q1')
# 
# # Import the MODIS land surface temperature collection.
# lst = ee.ImageCollection('MODIS/006/MOD11A1')
# 
# # Import the USGS ground elevation image.
# elv = ee.Image('USGS/SRTMGL1_003')
# =============================================================================




