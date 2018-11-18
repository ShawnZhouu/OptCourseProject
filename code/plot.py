# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:34:16 2018

@author: Shawn Z
"""

import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

fig = plt.figure(figsize=(20,10))
sns.set_style("darkgrid")
'''
fig.add_subplot(121)
plt.plot((ic['capex_to_assets'].index.to_pydatetime()), ic['capex_to_assets'].values)
plt.title('Factor IC of ' +'capex_to_assets',fontsize=16 )
fig.add_subplot(122)
plt.plot((ic['market_cap'].index.to_pydatetime()), ic['market_cap'].values)
plt.title('Factor IC of ' + 'market_cap', fontsize=16)
'''

plt.plot((ic['capex_to_assets'].index.to_pydatetime()[::20]), ic['capex_to_assets'].values[::20],label = 'Capex to Assets')
plt.plot((ic['market_cap'].index.to_pydatetime()[::20]), ic['market_cap'].values[::20],label='Market Cap')
plt.plot((ic['volatility_1y'].index.to_pydatetime()[::20]), ic['volatility_1y'].values[::20],label='Volatility 1y')
#plt.plot((ic['total_return_1m'].index.to_pydatetime()[::20]), ic['total_return_1m'].values[::20])
plt.legend(fontsize=15)
