# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 16:43:29 2018

@author: Shawn Z
"""

import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

'''Preprocess Data'''
mypath = 'C:/Users/Shawn Z/Spyder'
filenames = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and f.endswith('pickle'))]

factor = {}             #raw factor data
for f in filenames:
    f_ = f.replace('.pickle','')
    factor[f_] = pd.read_pickle(f)

ret_1m = pd.read_pickle('ret_future_1m.pickle')
factor.pop('ret_future_1m') #remove return from factor dictionary

ret_cur = pd.read_pickle('ret_current_1m.pickle')
factor.pop('ret_current_1m') #remove return from factor dictionary


