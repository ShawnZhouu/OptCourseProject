# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 18:39:56 2018

@author: Shawn Z
"""

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

ic_mean = pd.Series()
for f_ in factor.keys():
    ic_mean[f_] = ic[f_].mean()
    
ic_report=pd.DataFrame(index = factor.keys()) # ic summary 
ic_report['IC mean'] = ic_mean
ic_report['IC significance rate'] = sig_rate # ratio of significant days to all days
ic_report['|mean|*sig_rate'] = ic_report['IC significance rate']*abs(ic_report['IC mean'])

'''Current IC and p_value'''
ic_current = pd.Series()
p_value_current = pd.Series()
for f_ in factor.keys():
    ic_current[f_] = ic[f_][-1]
    # similar to last py file
    valid_columns = (~ret_1m.iloc[-1].isnull() & ~factor[f_].iloc[-1].isnull())
    p_value_current[f_] = stats.spearmanr(ret_1m.iloc[-1][valid_columns],factor[f_].iloc[-1][valid_columns] )[1]
    
ic_report['current IC'] = ic_current
ic_report['current significance'] = p_value_current<0.05



ic_report['current_IC to mean'] = ic_current/ic_report['IC mean']

#ic_report = ic_report.sort_values(by='mean*sig_rate', ascending = False)
#ic_report = ic_report[ic_report['IC significance rate']>0.5]