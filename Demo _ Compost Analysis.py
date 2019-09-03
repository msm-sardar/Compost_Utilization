# -*- coding: utf-8 -*-
"""
Created on Wed May 22 19:19:12 2019

@author: msmsa
"""
from project_class import *
from building_matrices import *
from Compost_use import *
from brightway2 import *
from CommonData import *
from time import time
from SWOLF_method import *


if __name__=='__main__':
    
    Treatment_processes = {}
    Treatment_processes['Compost_use']={'input_type':[],'model': Compost_use()}
    
    demo = project("Compost_use",Treatment_processes)
    demo.init_project('SWOLF_AccountMode_LCI DATA.csv')
    demo.write_project()
    demo.group_exchanges()
    import_methods()
        
#    demo.update_parameters(gg)
    
    scenario1 = {"Compost_use":{"Compost":1}}
    demo.process_start_scenario(scenario1,'scenario1')
    
    import pickle  
    file = open('Compost_use', 'wb')
    pickle.dump(demo, file)

project = "Compost_use"
projects.set_current(project)
db = Database("waste")
functional_unit = {db.get("scenario1") : 1}
method = ('SWOLF_IPCC','SWOLF')
A=LCA(functional_unit,method)
A.lci()
A.lcia()
print(A.score)
    








     
        
        
    





