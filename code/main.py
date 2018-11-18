# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 11:28:25 2018

@author: Shawn Z
"""

#ret_f = factor_ret(4)
#ret_f_,v_t,beta = wls(ret_f)
optimal_weight = opt(ret_f_,v_t,beta,500)
net_worth = simu(optimal_weight)
