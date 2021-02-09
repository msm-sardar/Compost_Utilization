 -*- coding: utf-8 -*-
"""
Created on Wed May 22 19:19:12 2019

@author: msmsa
"""
from project_class import *
from building_matrices import *
from Compost_use import *
from brightway2 import *
from time import time
from SWOLF_method import *
from AbioticDepletion import import_aibiotic_depletion

Treatment_processes = {}
Treatment_processes['Compost_use']={'input_type':[],'model': Compost_use()}

demo = project("Compost_use",Treatment_processes)
demo.init_project('SWOLF_AccountMode_LCI DATA.csv')
demo.write_project()
demo.group_exchanges()
import_methods()
import_aibiotic_depletion()
from Import_IPCC_new import *




scenario1 = {"Compost_use":{"Compost":1}}
demo.process_start_scenario(scenario1,'scenario1')
    
import pickle  
file = open('Compost_use', 'wb')
pickle.dump(demo, file)



method = ('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0, C1_36')
demo.Do_LCA("scenario1",method,1)

method = ('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1, C1_36')
demo.Do_LCA("scenario1",method,1)

method = ('IPCC 2007, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1')
demo.Do_LCA("scenario1",method,1)

method = ('IPCC 2007, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0')
demo.Do_LCA("scenario1",method,1)





project = "Compost_use"
projects.set_current(project)
db = Database("waste")
functional_unit = {db.get("scenario1") : 1}



method = ('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1, C1_36')
A=LCA(functional_unit,method)
A.lci()
A.lcia()
print(A.score)

method = ('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0, C1_36')
A=LCA(functional_unit,method)
A.lci()
A.lcia()
print(A.score)

method = ('IPCC 2007, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1')
A=LCA(functional_unit,method)
A.lci()
A.lcia()
print(A.score)

method = ('IPCC 2007, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0')
A=LCA(functional_unit,method)
A.lci()
A.lcia()
print(A.score)





db = Database("waste")
functional_unit = {db.get("scenario1") : 1}

db = Database("Technosphere")
functional_unit = {db.get('Nitrogen_Fertilizer') : 1}
functional_unit = {db.get('Phosphorous_Fertilizer') : 1}
functional_unit = {db.get('Potassium_Fertilizer') : 1}

method = ('CML (v4.4, 2015)', 'resources', 'depletion of abiotic resources - elements, ultimate reserves')
method = ('CML 2001 w/o LT (obsolete)',
  'resources w/o LT',
  'depletion of abiotic resources w/o LT')

A=LCA(functional_unit,method)
A.lci()
A.lcia()
print(A.score)







method = ('SWOLF_Acidification','SWOLF')
A=LCA(functional_unit,method)
A.lci()
A.lcia()
print(A.score)

method = ('SWOLF_Eutrophication','SWOLF')
A=LCA(functional_unit,method)
A.lci()
A.lcia()
print(A.score)

method = ('SWOLF_CED','SWOLF')
A=LCA(functional_unit,method)
A.lci()
A.lcia()
print(A.score)





project = "Compost_use"
projects.set_current(project)
db = Database("Technosphere")
functional_unit = {db.get("Electricity_consumption") : 1}
functional_unit = {db.get('Equipment_Diesel') : 1}
functional_unit = {db.get('Nitrogen_Fertilizer') : 1}
functional_unit = {db.get('Phosphorous_Fertilizer') : 1}
functional_unit = {db.get('Potassium_Fertilizer') : 1}
functional_unit = {db.get('Peat') : 1}
functional_unit = {db.get('market_for_excavation_skid_steer_loader' ) : 1}

method = ('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1, C1_36')
method = ('SWOLF_Acidification','SWOLF')
method = ('SWOLF_Eutrophication','SWOLF')
method = ('SWOLF_CED','SWOLF')
method = ('CML (v4.4, 2015)', 'resources', 'depletion of abiotic resources - elements, ultimate reserves')

A=LCA(functional_unit,method)
A.lci()
A.lcia()
print(A.score)
