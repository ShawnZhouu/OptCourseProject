
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

plt.subplots_adjust(top=3, bottom=1, left=0, right=4, hspace=0.3,wspace=0.25)

plt.subplot(1,2,1)

p=plt.scatter(vol_pre2,vol_test,s=20,marker='+',c=np.abs(np.array(vol_pre2)-np.array(vol_test)))
cbar=plt.colorbar(p)
cbar.set_label('L1 Distance')
plt.plot(np.linspace(-0.4,0,1000),1.2*np.linspace(-0.4,0,1000)-0.1,c=(0.6,0.1,0.5),label="Prediction = Reality")
#plt.plot(np.linspace(-1.1,0.5,1000),np.linspace(-1.5,0.5,1000),'r',label="Prediction = Reality")
plt.ylabel('Volatility Prediction',fontsize=15)
plt.xlabel('Volatility Reality',fontsize=15)
plt.title('One Feature (PE) Prediction vs Reality',fontsize=18)
plt.legend(loc=2)

plt.subplot(1,2,2)

p=plt.scatter(yh,y,marker='+',c=np.abs(np.array(yh)-np.array(y)))
cbar=plt.colorbar(p)
cbar.set_label('L1 Distance')
plt.plot(np.linspace(-1.5,0.5,1000),np.linspace(-1.5,0.5,1000),'r',label="Prediction = Reality")
plt.xlabel('Volatility Prediction',fontsize=15)
plt.ylabel('Volatility Reality',fontsize=15)
plt.title('Prediction vs Reality',fontsize=18)
plt.legend(loc=2)

# In[ ]:



