# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:17:37 2019

@author: msardar2
"""
import pandas as pd
from ast import literal_eval
from brightway2 import *

Data_1 = pd.read_excel('IPCC.xlsx',sheet_name = '2013',dtype={'Key':object})
IPCC2013_1=[]
IPCC2013_2=[]
for i in range(len(Data_1.Key)):
    IPCC2013_1.append((literal_eval(Data_1['Key'][i]), Data_1['IPCC 2013, Ecoinvent V3.5, climate change, GWP 100a, bioCO2=0'][i]))
    IPCC2013_2.append((literal_eval(Data_1['Key'][i]), Data_1['IPCC 2013, Ecoinvent V3.5, climate change, GWP 100a, bioCO2=1'][i]))

Method(('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0')).register()
Method(('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0')).write(IPCC2013_1)    

Method(('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1')).register()
Method(('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1')).write(IPCC2013_2) 

Data_2 = pd.read_excel('IPCC.xlsx',sheet_name = '2007')
IPCC2007_1=[]
IPCC2007_2=[]
for i in range(len(Data_2.Key)):
    IPCC2007_1.append((literal_eval(Data_2['Key'][i]), Data_2['IPCC 2007, Ecoinvent V3.5, climate change, GWP 100a, bioCO2=0'][i]))
    IPCC2007_2.append((literal_eval(Data_2['Key'][i]), Data_2['IPCC 2007, Ecoinvent V3.5, climate change, GWP 100a, bioCO2=1'][i]))

Method(('IPCC 2007, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0')).register()
Method(('IPCC 2007, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0')).write(IPCC2007_1)    

Method(('IPCC 2007, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1')).register()
Method(('IPCC 2007, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1')).write(IPCC2007_2) 

Data_3 = pd.read_excel('IPCC.xlsx',sheet_name = '2013 (C1 = 36)')
IPCC2013_3=[]
IPCC2013_4=[]
for i in range(len(Data_3.Key)):
    IPCC2013_3.append((literal_eval(Data_3['Key'][i]), Data_3['IPCC 2013, Ecoinvent V3.5, climate change, GWP 100a, bioCO2=0, C1_36'][i]))
    IPCC2013_4.append((literal_eval(Data_3['Key'][i]), Data_3['IPCC 2013, Ecoinvent V3.5, climate change, GWP 100a, bioCO2=1, C1_36'][i]))

Method(('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0, C1_36')).register()
Method(('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0, C1_36')).write(IPCC2013_3)    

Method(('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1, C1_36')).register()
Method(('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1, C1_36')).write(IPCC2013_4) 

methods.flush()


# =============================================================================
# 
# m=[('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1'),
#    ('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0'),
#    ('IPCC 2007, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0'),
#    ('IPCC 2007, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1'),
#    ('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0, C1_36'),
#    ('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1, C1_36')]
# 
# 
# for x in m:
#     method = x
#     demand = {('Technosphere', 'Electricity_consumption'):1}
#     A = LCA(demand, method)
#     A.lci()
#     A.lcia()
#     print(x,'\n',A.score,'\n','\n')
# =============================================================================

