# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 15:43:40 2018

@author: Shawn Z
"""

from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def weight(n_s):
    
    w = np.ones(n_s)
    for i in range(n_s-1):
        w[i+1] = w[i]/(1-0.005)
    return w/sum(w)



def wls(ret_f):
    ret_f_ = ret_f[['net_debt_12m_to_ebitda_12m',
     'ebit_12m_to_interst_expense_12m',
     'capex_to_assets',
     'cash_to_total_assets',
     'EPS_growth_12m',
     'fcf_yield_12m',
     'dividend_indicated_yield',
     'total_return_6m',
     'dividend_to_net_income',
     'total_return_12m',
     'total_assets',
     'price_to_52_week_high',
     'total_return_1m',
     'market_cap',
     'price_to_200ma',
     'net_income_5y_growth_rate',
     'total_assets_5_year_growth',
     'net_income_12m',
     'volatility_1y',
     'roe_avg_3y']]
    
    beta=pd.DataFrame(index = ret_f_.index[252::20], columns = ret_cur.columns)
    alpha=pd.DataFrame(index = ret_f_.index[252::20], columns = ret_cur.columns)
    v_t = dict(keys = ret_f_.index[252::20])
    for date in ret_f_.index[252::20]:
        i = ret_f_.index.get_loc(date)
        elist = [] #residual list
        for stock in ret_cur.columns:
            lr = LinearRegression()
            l = len(ret_f_[:i+1])
            lr.fit(ret_f_[:i+1], ret_cur[stock][:i+1], weight(l))
    
            beta[stock][date] = lr.coef_
            alpha[stock][date] = lr.intercept_
            
            elist.append(np.var(lr.predict(ret_f_[:i+1]) - ret_cur[stock][:i+1])) #residual variance of a single stock
            
        F = np.matrix(np.cov(ret_f_[:i+1].astype(float), aweights =weight(l), rowvar = False)) # compute factor returns cov matrix
        #print(F.shape)
        # e[date]= np.diag(elist)
        B = np.matrix(beta.loc[date].tolist())
        V = B*F*B.T + np.diag(elist)
        v_t[date] = V
    
    return ret_f_, v_t,beta

    
    