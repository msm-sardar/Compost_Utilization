from project_class import *
from building_matrices import *
import pickle
from CommonData import *
from Compost_use import *
from time import time
from Store_results import *
from brightway2 import *
if __name__=='__main__':
    demo = pickle.load(open("Compost_use","rb"))

    project = "Compost_use"
    projects.set_current(project)
    db = Database("waste")
    functional_unit = {db.get("scenario1") : 1}
    method = [('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1, C1_36'),
              ('IPCC 2013, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0, C1_36'),
              ('IPCC 2007, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=1'),
              ('IPCC 2007, Ecoinvent V3.5', 'climate change', 'GWP 100a, bioCO2=0'),
              ('SWOLF_Acidification','SWOLF'),
              ('SWOLF_Eutrophication','SWOLF'),
              ('SWOLF_PhotochemicalSmog','SWOLF'),
              ('SWOLF_CED','SWOLF')
              ]

    Treatment_processes = {}
    Treatment_processes['Compost_use']={'input_type':[],'model': Compost_use()}

    process_models = list()
    process_model_names = list()
    process_models.append(Treatment_processes['Compost_use']['model'])
    process_model_names.append('Compost_use')
    
    CommonData = CommonData()
     
    t1 = time()
    n=20000
    a = ParallelData(functional_unit, method, project,process_models=process_models,process_model_names=process_model_names,common_data =CommonData ,seed = 100)
    a.run(8,n)
    t2=time()
    print(n, 'runs in: ', t2-t1)
    
    Results=store_results(a.results)
    AAA = Results
    #Results.to_pickle('BU1_Peat')
    #Results=pd.read_pickle('BU1_Peat')


    
# =============================================================================
# contour plots
# ('initflow', 'C_cont')
# 'list': np.linspace(0.10,0.47,10).tolist()*10
# ('Lanfill', 'percCStor_LF')
# 'list': np.repeat(np.linspace(40,100,10),10)
# 
# 
# =============================================================================

# =============================================================================
# 
# ('Land_app', 'PeatSubFac')
# 'list': np.linspace(0,1,10).tolist()*10
# ('Land_app', 'densPeat')
# 'list': np.repeat(np.linspace(100,600,10),10)
# 
# =============================================================================


# =============================================================================
# ('initflow', 'C_cont')
# 'list':np.repeat(np.linspace(0.10,0.47,10),10)
# ('Material_Properties', 'mcFC')
# 'list':np.linspace(0.18,0.67,10).tolist()*10
# =============================================================================

# ('initflow', 'N_cont')
# 'list':np.repeat(np.linspace(0.0051,0.028,10),10)
# MFEN
# 'list':np.linspace(0,1,10).tolist()*10


        