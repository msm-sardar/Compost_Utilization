# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:47:19 2020

@author: msmsa
"""
from stats_arrays import *
import numpy as np

list_var = [{'name':'test','uncertainty_type':2,'loc': 2, 'scale':.3}]
Vars  = UncertaintyBase.from_dicts(*list_var)
rand = MCRandomNumberGenerator(Vars)
AA=rand.generate(100000)

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('figure', figsize=(10, 6))
matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20)
plt.hist(AA[0],bins=100)
plt.hist(np.log(AA[0]),bins=100)



list_var = [{'name':'test','uncertainty_type':2,'loc': 0.62058, 'scale':0.06206}]
Vars  = UncertaintyBase.from_dicts(*list_var)
rand = MCRandomNumberGenerator(Vars)
AA=rand.generate(10000)

plt.hist(AA[0],bins=20)

plt.hist(np.log(AA[0]),bins=20)



class mojtaba:
    def __init__(self):
        self.n = 2
        self.m = 4
A = mojtaba()
vars(A)




import matplotlib.pyplot as plt
import matplotlib

AA=np.random.normal(loc=20,scale=5,size=10000)
matplotlib.rc('figure', figsize=(10, 6))
matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20)
plt.hist(AA,bins=100)
plt.hist(np.exp(AA),bins=200)

AA=np.random.lognormal(mean=7, sigma=1,size=10000)
plt.hist(AA,bins=100)


A = 0.8
A = 2.29
A = 1.86
A = 15
mean = np.log(A)
sigma = np.abs(np.log(A))/2*0.2
AA=np.random.lognormal(mean=mean, sigma=sigma ,size=10000)
plt.hist(AA,bins=20)
print('L({}, {})'.format(np.round(mean,3),np.round(sigma,3)))
print('L({}, {})'.format(np.round(mean,5),np.round(sigma,5)))

AA=np.random.normal(loc=20,scale=5,size=10000)
plt.hist(AA,bins=100)


mean = np.log(20**2/np.sqrt(5+20**2))
print(mean)
sigma = np.sqrt(np.log(5/20**2+1))
print(sigma) 
AA=np.random.lognormal(mean=mean, sigma=sigma ,size=10000)
plt.hist(AA,bins=100)

AA=np.random.lognormal(mean=mean, sigma=0.747 ,size=10000)
plt.hist(AA,bins=100)


E = np.exp(mean+sigma**2/2)
print(E)
V = np.exp(2*mean - sigma**2)*(np.exp(sigma**2)-1)
print(V)



AA=np.random.lognormal(mean=-0.223, sigma=0.186 ,size=10000)
plt.hist(AA,bins=30)



gm = 0.055778
sigma  = 0.0006
mean = -2.89


