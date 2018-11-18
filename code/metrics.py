# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 11:21:29 2018

@author: Shawn Z
"""

def annual_return(capital_list):
    return (capital_list[-1]- 1)*(12 / len(capital_list[1:]))
    
def maximum_drawdown(capital_list):
    md = 0
    for i in range(1, len(capital_list)):
        if capital_list[i] / max(capital_list[:i]) - 1 < md:
            md = capital_list[i] / max(capital_list[:i]) - 1
    return md

def sharpe_ratio(capital_list):
    return annual_return(capital_list) / np.std(capital_list[1:])

print('annualized return:',annual_return(net_worth))
print('SR:',sharpe_ratio(net_worth))
print('max_drawdown',maximum_drawdown(net_worth))