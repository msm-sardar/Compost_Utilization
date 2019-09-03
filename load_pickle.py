from project_class import *
from building_matrices import *
import pickle
from building_matrices import *
from CommonData import *
from Compost_use import *
from time import time

if __name__=='__main__':
    demo = pickle.load(open("Compost_use","rb"))
    
    project = "Compost_use"
    projects.set_current(project)
    db = Database("waste")
    functional_unit = {db.get("scenario1") : 1}
    method = [('SWOLF_IPCC','SWOLF')]
    
    Treatment_processes = {}
    Treatment_processes['Compost_use']={'input_type':[],'model': Compost_use()}

    process_models = list()
    process_model_names = list()
    process_models.append(Treatment_processes['Compost_use']['model'])
    process_model_names.append('Compost_use')
    
    CommonData = CommonData()
     
    t1 = time()
    n=100
    a = ParallelData(functional_unit, method, project,process_models=process_models,process_model_names=process_model_names,common_data =CommonData ,seed = 1)
    a.run(4,n)
    t2=time()
    print(n, 'runs in: ', t2-t1)
    