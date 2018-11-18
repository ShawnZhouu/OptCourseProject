# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:12:04 2017

@author: Shawn Z
"""

import matplotlib.pyplot as plt

vol=(pd.read_csv('NYSE Volatility.csv',index_col='Date'))

plt.subplots_adjust(top=1, bottom=0, left=0, right=3, hspace=0.45,wspace=0.1)

plt.subplot(1,2,1)
vol['AA US Equity_y'].plot(c='purple')
plt.title('Volatility of Alcoa Corporation',fontsize=15)
plt.grid()

plt.subplot(1,2,2)
vol['AAV US Equity'].plot(c='purple')
plt.title('Volatility of Advantage Oil & Gas Ltd',fontsize=15)
plt.grid()