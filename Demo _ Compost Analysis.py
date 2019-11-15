# -*- coding: utf-8 -*-
"""
Created on Wed May 22 19:19:12 2019

@author: msmsa
"""
from project_class import *
from building_matrices import *
from Compost_use_1 import *
from brightway2 import *
from time import time
from SWOLF_method import *



    
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
file = open('test', 'wb')
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
    


demo.Do_LCA("scenario1",method,1)




# =============================================================================
# from stats_arrays import *
# import matplotlib.pyplot as plt
# comp = UncertaintyBase.from_dicts({'uncertainty_type':2,'loc': -0.59, 'scale':0.34,'minimum':0.08})
# comp_rng = MCRandomNumberGenerator(comp,seed=123)
# AA=[comp_rng.next() for i in range(10000)] 
# AA = [x[0] for x in AA]
# plt.hist(AA,bins=10)
# 
# =============================================================================
     
B= LCA({('waste','scenario1'):1},('SWOLF_Acidification','SWOLF'))
B.lci()
B.lcia()
print(B.score)
B.top_activities()
B.top_emissions()
        
    





