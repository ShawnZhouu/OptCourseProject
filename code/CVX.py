# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:41:30 2018

@author: Shawn Z
"""

import pandas as pd
from cvxpy import *

def opt(ret_f_, v_t, beta,gamma):
    ret_f_ = pd.read_pickle('ret_selected_20.pickle')
    ret_1m = pd.read_pickle('ret_future_1m.pickle')
    
    l = len(ret_1m.columns)
    
    stock_expected_ret = pd.Series()
    optimal_weight = {}
    optimal_risk = {}
    optimal_ret = {}
    
    for date in ret_f_.index[252::20]:
        i = ret_f_.index.get_loc(date)

        for stock in ret_1m.columns:
            
            stock_expected_ret[stock] = sum(beta.loc[date][stock]*ret_f_.loc[date]) + alpha[stock][date]
        
        x = Variable(l)
        
        ret = x.T*np.array(stock_expected_ret.tolist())
        risk = quad_form(x,v_t[date])
        
        obj =  Maximize(ret - gamma * risk)
        constraints = [sum_entries(x)==1,
                       norm(x, 1) <= 1.5,
                       max_entries(x)<=0.1]
        prob = Problem(obj, constraints)
        prob.solve()
        
        optimal_weight[date] = x.value
        optimal_risk[date] = risk.value
        optimal_ret[date] = ret.value
    
    return(optimal_weight)