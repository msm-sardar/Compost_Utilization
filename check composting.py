# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:21:58 2019

@author: msmsa
"""

from time import time
from Composting import *
from WTE import *
A= time()
B = Comp()
for i in range(100):
    B.calc()
    B.calc2()
    
print(time()-A)    

A= time()
B = WTE()
for i in range(100):
    B.calc()
print(time()-A)    