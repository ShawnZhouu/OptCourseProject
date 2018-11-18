# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:54:54 2017

@author: Shawn Z
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

def standardize(feature):
    return (feature-feature.mean(axis=0))/feature.std(axis=0)



vol=standardize(pd.read_csv('NYSE Volatility.csv').set_index('Date'))[-10:]

close=standardize(pd.read_csv('NYSE Close.csv',index_col='Date'))
pe=standardize(pd.read_csv('NYSE PE.csv',index_col='Date').shift(1))[-10:]
fcf=standardize(pd.read_csv('NYSE FCF per share.csv',index_col='Date').shift(1)[1:])[-10:]
invested_capital=standardize(pd.read_csv('NYSE Invested Capital.csv',index_col='Date').shift(1))[-10:]
dta=standardize(pd.read_csv('NYSE Debt to Asset.csv',index_col='Date').shift(1))[-10:]
dte=standardize(pd.read_csv('NYSE Debt to Equity.csv',index_col='Date').shift(1))[-10:]
cr=standardize(pd.read_csv('NYSE Current Ratio.csv',index_col='Date').shift(1))[-10:]
asset_turnover=standardize(pd.read_csv('NYSE Asset Turnover.csv',index_col='Date').shift(1))[-10:]

fig = plt.figure(figsize=(10,7.5))

plt.subplots_adjust(top=2, bottom=-1, left=0, right=1.5, hspace=0.3,wspace=0.25)

 
plt.subplot(4,2,1)
p=plt.scatter(pe,vol,c=close)
cbar=plt.colorbar(p)
cbar.set_label('Close Price', fontsize=18)
plt.title('Vol-PE', fontsize=20)
plt.xlabel('PE' , fontsize=18)
plt.ylabel('Vol')
    
plt.subplot(4,2,2)
p2=plt.scatter(fcf,vol,c=close)
cbar=plt.colorbar(p)
cbar.set_label('Close Price', fontsize=18)
plt.title('Vol-FCF',fontsize=20 )
plt.xlabel('FCF', fontsize=18)
plt.ylabel('Vol', fontsize=18)

#plt.plot(vol.mean(axis=1))
plt.subplot(4,2,3)
plt.scatter(invested_capital,vol,c=close)
cbar=plt.colorbar(p)
plt.title('Vol-Invested Capital', fontsize=20)
plt.xlabel('Invested Capital', fontsize=18)
plt.ylabel('Vol', fontsize=18)
cbar.set_label('Close Price', fontsize=18)

plt.subplot(4,2,4)
plt.scatter(dta,vol,c=close)
plt.title('Vol-Debt to Asset', fontsize=20)
plt.xlabel('Debt to Asset', fontsize=18)
plt.ylabel('Vol', fontsize=18)
cbar=plt.colorbar(p)
cbar.set_label('Close Price', fontsize=18)