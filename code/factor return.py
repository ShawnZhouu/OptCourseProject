# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 14:31:43 2018

@author: Shawn Z
"""
import pandas as pd



def factor_ret(window):
    ret_f = pd.DataFrame(index = ret_cur.index, columns=factor.keys())
    for f_ in factor.keys():
        for date in ret_cur.index:
            if len(factor[f_])==811:
                i = ret_cur.index.get_loc(date)
                s = 0
                for ind in range((i - window*20),i+1,20):
                    
                    valid = factor[f_].iloc[ind].dropna()
                    l = int(len(valid) * 0.2)
                    top20 = valid.sort_values(ascending = False)[:l].index
                    bot20 = valid.sort_values(ascending = False)[-l:].index
                    s += (ret_cur.iloc[ind][top20].mean()-ret_cur.iloc[ind][bot20].mean())/2
                s = s/window   
            
                ret_f[f_][date] = s*(ic[f_][i-20:i+1].mean()/ic[f_][i-60:i+1].mean()+1)

    return ret_f
        

