# -*- coding: utf-8 -*-
"""
Created on Wed May 22 19:19:12 2019

@author: msmsa
"""
from project_class import *
from building_matrices import *
from AD import *
from Composting import *
from brightway2 import *
from CommonData import *
from time import time
from SWOLF_method import *


if __name__=='__main__':
    
    Treatment_processes = {}
    Treatment_processes['AD']={'input_type':['MOC','Separated_Organics'],'model': AD()}
    Treatment_processes['COMP']={'input_type':['MOC','Separated_Organics'], 'model': Comp()}
    Treatment_processes['LF']={'path':"trad_landfill _BW2.xlsx",'input_type':['MWC','RWC','Bottom_Ash','Fly_Ash','Other_Residual']}
    
    demo = project("Organic_Analysis",Treatment_processes)
    demo.init_project('SWOLF_AccountMode_LCI DATA.csv')
    demo.write_project()
    demo.group_exchanges()
    import_methods()
    
    gg=[{'name': 'frac_of_Other_Residual_from_AD_to_LF', 'amount': 1},
         {'name': 'frac_of_Other_Residual_from_COMP_to_LF', 'amount': 1},
         {'name': 'frac_of_Bottom_Ash_from_LF_to_LF', 'amount': 1},
         {'name': 'frac_of_Fly_Ash_from_LF_to_LF', 'amount': 1},
         {'name': 'frac_of_Separated_Organics_from_LF_to_AD', 'amount': 0.5},
         {'name': 'frac_of_Separated_Organics_from_LF_to_COMP', 'amount': 0.5},
         {'name': 'frac_of_Other_Residual_from_LF_to_LF', 'amount': 1}]
        
    demo.update_parameters(gg)
    
    scenario1 = {"AD":{"Yard_Trimmings_Leaves":1}}
    scenario2 = {"AD":{"Yard_Trimmings_Grass":1}}
    scenario3 = {"AD":{"Yard_Trimmings_Branches":1}}
    scenario4 = {"AD":{"Food_Waste_Vegetable":1}}
    scenario5 = {"AD":{"Food_Waste_Non_Vegetable":1}}
    
    scenario6 = {"COMP":{"Yard_Trimmings_Leaves":1}}
    scenario7 = {"COMP":{"Yard_Trimmings_Grass":1}}
    scenario8 = {"COMP":{"Yard_Trimmings_Branches":1}}
    scenario9 = {"COMP":{"Food_Waste_Vegetable":1}}
    scenario10 = {"COMP":{"Food_Waste_Non_Vegetable":1}}
    
    scenario11 = {"COMP":{"Food_Waste_Vegetable":1},"AD":{"Yard_Trimmings_Leaves":1}}
    
    demo.process_start_scenario(scenario1,'scenario1')
    demo.process_start_scenario(scenario2,'scenario2')
    demo.process_start_scenario(scenario3,'scenario3')
    demo.process_start_scenario(scenario4,'scenario4')
    demo.process_start_scenario(scenario5,'scenario5')
    demo.process_start_scenario(scenario6,'scenario6')
    demo.process_start_scenario(scenario7,'scenario7')
    demo.process_start_scenario(scenario8,'scenario8')
    demo.process_start_scenario(scenario9,'scenario9')
    demo.process_start_scenario(scenario10,'scenario10')
    demo.process_start_scenario(scenario10,'scenario11')
   
    
    
    import pickle  
    file = open('OrganicAnalysis', 'wb')
    pickle.dump(demo, file)
    
    
    
    
    
    
    
    demo.Do_LCA("scenario5",('SWOLF_IPCC','SWOLF'),1)
    demo.Do_LCA("scenario4",('SWOLF_Acidification','SWOLF'),1)
    demo.Do_LCA("scenario6",('SWOLF_Eutrophication','SWOLF'),1)
    demo.Do_LCA("scenario6",('SWOLF_PhotochemicalSmog','SWOLF'),1)
    demo.Do_LCA("scenario6",('SWOLF_CED','SWOLF'),1)
    




    
from building_matrices import *
from CommonData import *
if __name__=='__main__':    
    CommonData = CommonData()
    CommonData.Land_app = {
            'cmpLandDies':{"Name":"Compost application diesel use","amount":0.8,"unit":'L/Mg compost',"Reference":None,},
            
            'NO3runoff':{"Name":"Nitrogen runoff to surface water","amount":0.14,"unit":'kg N/kg N applied',"Reference":None,
                         'uncertainty_type':3,'loc':0.2,'scale':0.1,'minimum':0.03,'maximum':0.4},
                         
            'NO3leach':{"Name":"Nitrogen leaching to ground water","amount":0.135,"unit":'kg N/kg N applied',"Reference":'23',
                        'uncertainty_type':3,'loc':0.2,'scale':0.1,'minimum':0.03,'maximum':0.4},
                        
            'MFEN':{"Name":"Nitrogen mineral fertilizer equivalent","amount":0.4,"unit":'kg N/kg N applied',"Reference":None,
                    'uncertainty_type':3,'loc':0.5,'scale':0.3,'minimum':0.2,'maximum':1},
            
            'MFEP':{"Name":"Phosphorus mineral fertilizer equivalent","amount":1,"unit":'kg N/kg N applied',"Reference":None,
                    'uncertainty_type':3,'loc':0.6,'scale':0.2,'minimum':0.2,'maximum':1},
                    
            'MFEK':{"Name":"Potassium mineral fertilizer equivalent","amount":1,"unit":'kg N/kg N applied',"Reference":None,
                    'uncertainty_type':3,'loc':0.6,'scale':0.2,'minimum':0.2,'maximum':1},
            
            'DslAppN':{"Name":"Fertilizer - Diesel fuel for application per kg N","amount":0.00229 ,"unit":'L/kg',"Reference":None},
            'DslAppP':{"Name":"Fertilizer - Diesel fuel for application per kg P","amount":0.00186 ,"unit":'L/kg',"Reference":None},
            'DslAppK':{"Name":"Fertilizer - Diesel fuel for application per kg K","amount":0.00125 ,"unit":'L/kg',"Reference":None},
            
            'fert_NO3Run':{"Name":"Fertilizer - Nitrate runoff to surface water","amount":10 ,"unit":'%',"Reference":None,
                           'uncertainty_type':3,'loc':0.1,'scale':0.05,'minimum':0.01,'maximum':0.25},
                           
            'fert_NO3Leach':{"Name":"Fertilizer - Nitrate leaching to ground water","amount":10 ,"unit":'%',"Reference":None,
                             'uncertainty_type':3,'loc':0.1,'scale':0.05,'minimum':0.01,'maximum':0.25},
                             
            'fert_N2O':{"Name":"Fertilizer - N released as N2O","amount":2.3 ,"unit":'%',"Reference":None,
                       'uncertainty_type':3,'loc':2,'scale':0.5,'minimum':1,'maximum':3 },
                        
            'fert_NH3':{"Name":"Fertilizer - N as NH3","amount":50 ,"unit":'%',"Reference":None,
                         'uncertainty_type':3,'loc':20,'scale':5,'minimum':0,'maximum':40},
                        
            'fert_NH3Evap':{"Name":"Fertilizer - NH3 evaporated","amount":5 ,"unit":'%',"Reference":None,
                            'uncertainty_type':3,'loc':5,'scale':3,'minimum':0,'maximum':15}
                    }
            
    CommonData.Organic_analysis = {
                'choice_BU':{"Name":"Offset Beneficial Use of Compost? (0=no; 1=yes)","amount":1,"unit":None,"Reference":None},
                             
                'peatOff':{"Name":"Soil amendment offset peat (1) or no (0)","amount":0,"unit":None,"Reference":None,
                           'uncertainty_type':7,'minimum':0,'maximum':2},
                           
                'fertOff':{"Name":"Soil amendment offset fertilizer (1) or no (0)","amount":1,"unit":None,"Reference":None,
                           'uncertainty_type':7,'minimum':0,'maximum':2},
                
                'perN2Oevap':{"Name":"Percent of applied N evaporated as N2O","amount":1.5,"unit":'%',"Reference":'16',
                              'uncertainty_type':3,'loc':3,'scale':1,'minimum':1,'maximum':5},
                              
                'perNH3evap':{"Name":"Percent of Ammonia that evaporates","amount":15,"unit":'%',"Reference":'16',
                              'uncertainty_type':3,'loc':10,'scale':4,'minimum':3,'maximum':20},
                              
                'perNasNH3fc':{"Name":"Percent N that is Ammonia","amount":50,"unit":'%',"Reference":'16',
                               'uncertainty_type':3,'loc':30,'scale':20,'minimum':0,'maximum':60}
                }
                         
    process_models = list()
    process_model_names = list()
    #process_models.append(Treatment_processes['AD']['model'])
    #process_model_names.append('AD')
    process_models.append(Treatment_processes['COMP']['model'])
    process_model_names.append('COMP')
    
    
    from time import time
    project = "Organic_Analysis"
    projects.set_current(project)
    db = Database("waste")
    functional_unit = {db.get("scenario9") : 1}
    method = ('SWOLF_IPCC','SWOLF')
    
    t1 = time()
    n=1000
    a = ParallelData(functional_unit, method, project,process_models=process_models,process_model_names=process_model_names,parameters=demo.unified_params,common_data=CommonData,seed = 1)
    a.run(4,n)
    t2=time()
    print(n, 'runs in: ', t2-t1)
    
    
# =============================================================================
#     from matplotlib.pylab import *
#     hist(a.results, density=True, histtype="step")
#     xlabel('(IPCC 2007, climate change, GWP 100a)')
#     ylabel("Probability")
# =============================================================================
    






db = Database("waste")
functional_unit = {db.get("scenario6") : 1}
method = ('SWOLF_IPCC','SWOLF')
C=LCA(functional_unit,method)
C.lci()
C.lcia()
print(C.score)

db = Database("Technosphere")
functional_unit = {db.get('Equipment_Diesel') : 7.33-5.7}
method = ('SWOLF_IPCC','SWOLF')
C=LCA(functional_unit,method)
C.lci()
C.lcia()
print(C.score)








     
        
        
    





