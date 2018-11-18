
# coding: utf-8

# In[45]:

import pandas
import numpy as np
import statsmodels.formula.api as sm
import sklearn.preprocessing
import matplotlib.pyplot as plt


# In[46]:

def standardize(feature):
    return (feature-feature.mean(axis=0))/feature.std(axis=0)


# In[74]:

Volatility = pandas.read_csv('NYSE Volatility.csv',index_col='Date')
Asset_Turnover = pandas.read_csv('NYSE Asset Turnover.csv',index_col='Date')
FCF = pandas.read_csv('NYSE FCF per share.csv',index_col='Date')
Current_Ratio = pandas.read_csv('NYSE Current Ratio.csv',index_col='Date')
D_A = pandas.read_csv('NYSE Debt to Asset.csv',index_col='Date')
D_E = pandas.read_csv('NYSE Debt to Equity.csv',index_col='Date')
Invested_Capital = pandas.read_csv('NYSE Invested Capital.csv',index_col='Date')
PE = pandas.read_csv('NYSE PE.csv',index_col='Date')

Volatility = standardize(Volatility)
Asset_Turnover = standardize(Asset_Turnover)
FCF = standardize(FCF)
Current_Ratio = standardize(Current_Ratio)
D_A = standardize(D_A)
D_E = standardize(D_E)
Invested_Capital = standardize(Invested_Capital)
PE = standardize(PE)


# In[76]:

vol = Volatility.drop(Volatility.index[0]).values.flatten()
asset_turnover = Asset_Turnover.drop(Asset_Turnover.index[33]).values.flatten()
fcf = FCF.drop(FCF.index[34]).drop(FCF.index[0]).values.flatten()
current_ratio = Current_Ratio.drop(Current_Ratio.index[33]).values.flatten()
d_a = D_A.drop(D_A.index[33]).values.flatten()
d_e = D_E.drop(D_E.index[33]).values.flatten()
invested_capital = Invested_Capital.drop(Invested_Capital.index[33]).values.flatten()
pe = PE.drop(PE.index[33]).values.flatten()


# In[77]:

np.size(d_a)==np.size(vol)


# In[78]:

# drop nan
vol = list(vol)
asset_turnover = list(asset_turnover)
fcf = list(fcf)
current_ratio = list(current_ratio)
d_a = list(d_a)
d_e = list(d_e)
invested_capital = list(invested_capital)
pe = list(pe)

i = 0
while i < len(vol):
    if (np.isnan(vol[i])) or (np.isnan(asset_turnover[i])) or (np.isnan(fcf[i])) or (np.isnan(current_ratio[i])) or (np.isnan(d_a[i])) or (np.isnan(d_e[i])) or (np.isnan(invested_capital[i])) or (np.isnan(pe[i])):
        vol.pop(i)
        asset_turnover.pop(i)
        fcf.pop(i)
        current_ratio.pop(i)
        d_a.pop(i)
        d_e.pop(i)
        invested_capital.pop(i)
        pe.pop(i)
    else:
        i = i + 1


# In[80]:

len(vol)


# In[81]:

# training set
vol_train = vol[:int(np.size(vol)*0.6)]
asset_turnover_train = asset_turnover[:int(np.size(asset_turnover)*0.6)]
fcf_train = fcf[:int(np.size(fcf)*0.6)]
current_ratio_train = current_ratio[:int(np.size(current_ratio)*0.6)]
d_a_train = d_a[:int(np.size(d_a)*0.6)]
d_e_train = d_e[:int(np.size(d_e)*0.6)]
invested_capital_train = invested_capital[:int(np.size(invested_capital)*0.6)]
pe_train = pe[:int(np.size(pe)*0.6)]

# test set
vol_test = vol[int(np.size(vol)*0.6):]
asset_turnover_test = asset_turnover[int(np.size(asset_turnover)*0.6):]
fcf_test = fcf[int(np.size(fcf)*0.6):]
current_ratio_test = current_ratio[int(np.size(current_ratio)*0.6):]
d_a_test = d_a[int(np.size(d_a)*0.6):]
d_e_test = d_e[int(np.size(d_e)*0.6):]
invested_capital_test = invested_capital[int(np.size(invested_capital)*0.6):]
pe_test = pe[int(np.size(pe)*0.6):]


# In[84]:

reg = pandas.DataFrame()
reg['Vol_train']=vol_train
reg['Asset_Turnover_train']=asset_turnover_train
reg['FCF_train']=fcf_train
reg['Current_Ratio_train']=current_ratio_train
reg['D_A_train']=d_a_train
reg['D_E_train']=d_e_train
reg['Invested_Capital_train']=invested_capital_train
reg['PE_train']=pe_train


# In[91]:

model = sm.ols(formula="Vol_train ~ Asset_Turnover_train + FCF_train + Current_Ratio_train + D_A_train + D_E_train + Invested_Capital_train + PE_train", data=reg).fit()
print(model.summary())


# In[92]:

w = np.array(model.params)


# In[93]:

vol_pre = []
for i in range(len(vol_test)):
    vol_pre.append(w[0] + w[1]*asset_turnover_test[i] + w[2]*fcf_test[i] + w[3]*current_ratio_test[i] + w[4]*d_a_test[i] + w[5]*d_e_test[i] + w[6]*invested_capital_test[i] + w[7]*pe_test[i])


# In[104]:

y=vol_test
yh=vol_pre

plt.subplot(1,2,2)

p=plt.scatter(vol_test,vol_pre,marker='+',c=np.abs(np.array(vol_pre)-np.array(vol_test)))
cbar=plt.colorbar(p)
cbar.set_label('L1 Distance')
plt.plot(np.linspace(-1.5,0.5,1000),np.linspace(-1.5,0.5,1000),'r',label="Prediction = Reality")
plt.ylabel('Volatility Prediction')
plt.xlabel('Volatility Reality')
plt.title('Prediction vs Reality')
plt.legend(loc=2)


# In[ ]:



