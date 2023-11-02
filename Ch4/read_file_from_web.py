#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 08:50:45 2023

@author: ethanpeacock
"""
from urllib.request import urlopen
import numpy as np
web_file = urlopen( "https://www.physics.upenn.edu/biophys/" + \
                    "PMLS/Datasets/01HIVseries/HIVseries.csv")
data_set = np.loadtxt(web_file, delimiter=',')
print(data_set)
    
