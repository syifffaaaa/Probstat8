#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from scipy.stats import chi2_contingency

data = np.array([[8, 22, 15, 5],
              [10, 28, 20,7],
              [12, 30, 20, 8]])

chi2, p, dof, expected = chi2_contingency(data)

print(f"Chi-Square Statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of Freedom: {dof}")
print(f"Expected Frequencies:")
print(expected)

alpha = 0.01
if p < alpha:
    print("Tolak H0: Terdapat hubungan antara kecukupan tidur dan kekuatan gowes.")
else:
    print("Gagal Tolak H0: Tidak terdapat hubungan antara kecukupan tidur dan kekuatan gowes.")


# In[2]:


import numpy as np
from scipy import stats

# Data sampel nilai dari 15 mahasiswa
data = [904, 920, 973, 1001, 1002, 1002, 1012, 1016, 1039, 1086, 1140, 1146, 1168, 1233, 1255, 1348]

# Melakukan Uji Kolmogorov-Smirnov
stat, p_value = stats.kstest(data, 'norm', args=(np.mean(data), np.std(data, ddof=1)))

print("Statistik Uji Kolmogorov-Smirnov:", stat)
print("p-value:", p_value)

# Menentukan apakah data berdistribusi normal atau tidak
alpha = 0.05
if p_value > alpha:
    print("Data berdistribusi normal (gagal menolak H0)")
else:
    print("Data tidak berdistribusi normal (menolak H0)")


# In[4]:


import numpy as np 
from scipy.stats import chi2_contingency

data = np.array([[14,6,9],
                [10, 16, 10],
                [2,13,20]])
chi2,p,dof,expected = chi2_contingency(data)

print(f"Chi-Square Statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of Freedom: {dof}")
print(f"Expected Frequencies:")
print(expected)

alpha = 0.01
if p<alpha:
    print("Tolak H0: Terdapat hubungan antara pendapatan dan mutu bahan makanan.")
else:
    print("Gagal Tolak H0: Tidak terdapat hubungan antara pendapatan dan mutu bahan makanan.)")


# In[6]:


import numpy as np
from scipy import stats

data = [8,11,12,22,24,25,33,34,34,43,45,45,67,67,99]

stat,p_value = stats.kstest(data,'norm',args=(np.mean(data),np.std(data,ddof=1)))

print("Statistik Uji Kolmogorov-Smirnov:",stat)
print("p_value:",p_value)

alpha = 0.05
if p_value>alpha:
    print("Data berdistribusi normal (gagal menolak H0.)")
else:
    print("Data tidak berdistribusi normal (menolak H0.)")
    


# In[ ]:




