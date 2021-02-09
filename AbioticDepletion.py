# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:53:03 2020

@author: msmsa
"""

import pandas as pd
from ast import literal_eval
from brightway2 import *

def import_aibiotic_depletion():

    Data = pd.read_excel('AbioticDepletion.xlsx')
    
    project = "Compost_use"
    projects.set_current(project)
    db = Database("biosphere3")
    
    Data['N'] = 0
    Data['key'] = None
    
    for i in Data.index:
        subset=db.search(Data['Flow2'][i])
        for act in subset:
                if act.as_dict()['categories'][0] == 'natural resource' and act.as_dict()['name'] == Data['Flow2'][i]:
                    Data.loc[i,'N'] +=1
                    Data.loc[i,'key'] = str(act.key)
                    
    CF = []
    for i in Data.index:
        CF.append((literal_eval(Data['key'][i]), Data['Factor2'][i]))
    
    Method(('CML (v4.4, 2015)', 'resources', 'depletion of abiotic resources - elements, ultimate reserves')).register()
    Method(('CML (v4.4, 2015)', 'resources', 'depletion of abiotic resources - elements, ultimate reserves')).write(CF)  