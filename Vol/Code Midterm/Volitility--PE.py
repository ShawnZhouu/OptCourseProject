
# coding: utf-8

# In[1]:

import pandas
import numpy as np
import statsmodels.formula.api as sm
import sklearn.preprocessing
import matplotlib.pyplot as plt


# In[2]:

def standardize(feature):
    return (feature-feature.mean(axis=0))/feature.std(axis=0)


# In[3]:

Volatility = pandas.read_csv('NYSE Volatility.csv',index_col='Date')
PE = pandas.read_csv('NYSE PE.csv',index_col='Date')

Volatility = standardize(Volatility)
PE = standardize(PE)


# In[4]:

vol = Volatility.drop(Volatility.index[0]).values.flatten()
pe = PE.drop(PE.index[33]).values.flatten()


# In[5]:

# drop nan
vol = list(vol)
pe = list(pe)

i = 0
while i < len(vol):
    if (np.isnan(vol[i])) or (np.isnan(pe[i])):
        vol.pop(i)
        pe.pop(i)
    else:
        i = i + 1


# In[10]:

# drop outlier
P_vol = np.percentile(vol, [2.5, 97.5])
P_pe = np.percentile(pe, [2.5, 97.5])
i = 0
while i < len(vol):
    if (vol[i]>P_vol[1]) or (vol[i]<P_vol[0]) or (pe[i]>P_pe[1]) or (pe[i]<P_pe[0]):
        vol.pop(i)
        pe.pop(i)
    else:
        i = i + 1


# In[11]:

# training set
vol_train = vol[:int(np.size(vol)*0.9)]
pe_train = pe[:int(np.size(pe)*0.9)]

# test set
vol_test = vol[int(np.size(vol)*0.1):]
pe_test = pe[int(np.size(pe)*0.1):]


# In[12]:

len(pe_test)


# In[13]:

reg = pandas.DataFrame()
reg['Vol_train']=vol_train
reg['PE_train']=pe_train


# In[14]:

model = sm.ols(formula="Vol_train ~ PE_train", data=reg).fit()
print(model.summary())


# In[15]:

w = np.array(model.params)


# In[17]:

vol_pre2 = []
for i in range(len(vol_test)):
    vol_pre2.append(w[0] + w[1]*pe_test[i])


# In[42]:

plt.scatter(vol_pre2,vol_test,s=0.1,c=(0.3,0.5,0.8))
plt.plot(np.linspace(-0.4,0,1000),1.2*np.linspace(-0.4,0,1000)-0.1,c=(0.6,0.1,0.5))
plt.show()


# In[ ]:



