# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:32:37 2019

@author: msardar2
"""
from brightway2 import *
project = "Compost_use"
projects.set_current(project)

method = [('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1, C1_36'),
              ('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0, C1_36'),
              ('IPCC 2007, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1'),
              ('IPCC 2007, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0'),
              ('SWOLF_Acidification','SWOLF'),
              ('SWOLF_Eutrophication','SWOLF'),
              ('SWOLF_PhotochemicalSmog','SWOLF'),
              ('SWOLF_CED','SWOLF')
              ]

tech= [('Technosphere', 'Electricity_production'),
       ('Technosphere', 'Equipment_Diesel'),
       ('Technosphere', 'Nitrogen_Fertilizer'),
       ('Technosphere', 'Phosphorous_Fertilizer'),
       ('Technosphere', 'Potassium_Fertilizer'),
       ('Technosphere', 'Peat'),
       ('Technosphere', 'market_for_excavation_skid_steer_loader'),
       ('Technosphere', 'compost_to_LF')
       ] 


import pandas as pd
AA= pd.DataFrame(columns=['tech_flow','method','score'])

C=[]
CC=[]
CCC=[]
for j in tech:
    for i in method:
        A= LCA({j:1},i)
        A.lci()
        A.lcia()
        C.append(j)
        CC.append(i)
        CCC.append(A.score)

AA['tech_flow']=C
AA['method']=CC
AA['score']=CCC