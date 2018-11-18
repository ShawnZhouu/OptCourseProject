# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 14:29:15 2018

@author: Shawn Z
"""


'''Generate IC Time Series'''
l = len(ret_1m)
ic = {}
sig_rate = pd.Series() 

for f_ in factor.keys():
    ic[f_]=pd.Series()
    sig_count = 0
    for i in ret_1m.index:
        valid_columns = (~ret_1m.loc[i].isnull() & ~factor[f_].loc[i].isnull())     #colmons valid on both return and factor
        spr = stats.spearmanr(factor[f_].loc[i][valid_columns], ret_1m.loc[i][valid_columns])
        ic[f_][i] = spr[0]
        sig_count += int(spr[1]<0.05)  # if p_value of one day < 0.05, count+1 
    sig_rate[f_] = sig_count/l    
    

