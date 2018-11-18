# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 22:35:12 2018

@author: Shawn Z
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def simu(optimal_weight):
    rebalence_date = ret_f_.index[252::20]
    ret_all = ret_1m.mean(axis = 1)
    net_worth = [1]
    temp = 1
    benchmark_worth = [1]
    for date in rebalance_date:
        
        i = ret_f_.index.get_loc(date)
        w = np.array(optimal_weight[date]).reshape(505)
        a = np.array(ret_1m.loc[date])*w
        temp += sum(a[~np.isnan(a)])
        net_worth.append(temp)
    
    
    benchmark_worth = np.cumsum([1] + list(ret_all[252::20]))
    
    #sp_worth.append(sp.iloc[i+20])
    fig = plt.figure(figsize=(16,8))    
    plt.plot(np.append(rebalance_date.to_pydatetime(), rebalance_date.to_pydatetime()[-1]+dt.timedelta(days=28)), net_worth, label = 'Stragegy')
    plt.plot(np.append(rebalance_date.to_pydatetime(), rebalance_date.to_pydatetime()[-1]+dt.timedelta(days=28)), benchmark_worth, label = 'Benchmark')
    plt.legend(loc = 2, fontsize = 16)
    plt.title('Time series approach', fontsize = 20)
    return net_worth
