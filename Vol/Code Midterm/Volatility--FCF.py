
# coding: utf-8

# In[2]:

import pandas
import numpy as np
import statsmodels.formula.api as sm
import sklearn.preprocessing
import matplotlib.pyplot as plt


# In[3]:

def standardize(feature):
    return (feature-feature.mean(axis=0))/feature.std(axis=0)


# In[4]:

Volatility = pandas.read_csv('NYSE Volatility.csv',index_col='Date')
FCF = pandas.read_csv('NYSE FCF per share.csv',index_col='Date')
Volatility = standardize(Volatility)
FCF = standardize(FCF)


# In[5]:

vol = Volatility.values.flatten()
fcf = FCF.drop(FCF.index[34]).values.flatten()


# In[6]:

# drop nan
vol = list(vol)
fcf = list(fcf)
i = 0
while i < len(vol):
    if (np.isnan(vol[i])) or (np.isnan(fcf[i])):
        vol.pop(i)
        fcf.pop(i)
    else:
        i = i + 1


# In[7]:

# drop outlier
P_vol = np.percentile(vol, [2.5, 97.5])
P_fcf = np.percentile(fcf, [2.5, 97.5])
i = 0
while i < len(vol):
    if (vol[i]>P_vol[1]) or (vol[i]<P_vol[0]) or (fcf[i]>P_fcf[1]) or (fcf[i]<P_fcf[0]):
        vol.pop(i)
        fcf.pop(i)
    else:
        i = i + 1


# In[9]:

# training set
vol_train = vol[:int(np.size(vol)*0.9)]
fcf_train = fcf[:int(np.size(fcf)*0.9)]

# test set
vol_test = vol[int(np.size(vol)*0.1):]
fcf_test = fcf[int(np.size(fcf)*0.1):]


# In[10]:

reg_fcf = pandas.DataFrame()
reg_fcf['Vol_train']=vol_train
reg_fcf['FCF_train']=fcf_train


# In[11]:

model_fcf = sm.ols(formula="Vol_train ~ FCF_train", data=reg_fcf).fit()
print(model_fcf.summary())


# In[12]:

w = np.array(model_fcf.params)
w


# In[14]:

vol_pre = []
for i in range(len(fcf_test)):
    vol_pre.append(w[0] + w[1]*fcf_test[i])


# In[16]:

plt.subplots_adjust(top=3, bottom=1, left=0, right=4, hspace=0.3,wspace=0.25)

plt.subplot(1,2,1)
p=plt.scatter(vol_test,vol_pre,s=20,marker='+',c=np.abs(np.array(vol_pre)-np.array(vol_test)))
cbar=plt.colorbar(p)
cbar.set_label('L1 Distance')
plt.plot(np.linspace(-.1,0.02,1000),np.linspace(-.1,0.02,1000),'r',label="Prediction = Reality")
plt.ylabel('Volatility Prediction')
plt.xlabel('Volatility Reality')
plt.title('One Feature (FCF) Prediction vs Reality',fontsize=18)
plt.legend(loc=2)


# In[ ]:



