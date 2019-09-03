# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:37:44 2019

@author: msardar2
"""
import pandas as pd
import numpy as np
from MC import *
class Compost_input(MC):
    def __init__(self):

### Land application inputs
        self.Land_app = {
                'distLand':{"Name":"Distance to application site","amount":20,"unit":'km',"Reference":None},
                'erLand':{"Name":"Empty return from land application (0=no; 1=yes)","amount":1,"unit":'0/1',"Reference":None},
                'land_payload':{"Name":"Actual payload of truck used to haul soil amendment","amount":7.3,"unit":'Mg',"Reference":None},
                'PeatSubFac':{"Name":"Volumetric peat replacement factor","amount":1,"unit":None,"Reference":'17'},
                
                'densPeat':{"Name":"Density of peat","amount":200,"unit":'kg/m3',"Reference":'17',
                            'uncertainty_type':5,'loc': 200 ,'minimum':150,'maximum':250},
                
                'perN2Oevap':{"Name":"Percent of applied N evaporated as N2O","amount":1.5,"unit":'%',"Reference":'16',
                              'uncertainty_type':5,'loc': 3 ,'minimum':1,'maximum':5},
                
                'perNH3evap':{"Name":"Percent of Ammonia that evaporates","amount":15,"unit":'%',"Reference":'16',
                              'uncertainty_type':5,'loc': 10 ,'minimum':3,'maximum':20},
                              
                'perNasNH3fc':{"Name":"Percent N that is Ammonia","amount":50,"unit":'%',"Reference":'16',
                               'uncertainty_type':5,'loc': 30 ,'minimum':0,'maximum':60},
                }  
        
### Facility Operation
        self.operation = {
                'choice_BU':{'Name':'Digestate Beneficial Use (1) or No Beneficial Use (0)','amount':1,'unit':'0/1','Referenc':None},
                'peatOff':{'Name':'Digestate Beneficial Use offsets Peat (1 - Yes; 0 - No)','amount':1,'unit':'0/1','Referenc':None},
                'fertOff':{'Name':'Digestate Beneficial Use offsets Fertilizer (1 - Yes; 0 - No)','amount':1,'unit':'0/1','Referenc':None},
                }

### Material Properties
        self.Material_Properties ={
            'mcFC':{'Name':'Finished compost moisture content','amount':0.45 ,'unit':'mass water/total mass','Referenc':None,
                    'uncertainty_type':5,'loc': 0.45 ,'minimum':.35,'maximum':0.55},
            'densFC':{'Name':'Density of final compost','amount':700 ,'unit':'kg/m3','Referenc':2,
                      'uncertainty_type':5,'loc': 700 ,'minimum':600,'maximum':800}
            }

### Soil Sequestration
        self.Soil_seq ={
                'perCStor':{"Name":"Percent of carbon in finished compost remaining after 100 years","amount":10,"unit":'%'
                            ,'uncertainty_type':5,'loc': 10 ,'minimum':2,'maximum':16},
                'humFormFac':{"Name":"100 year carbon storage from humus formation","amount":0,"unit":'kg-C/kg-C in compost',"Reference":'4'}
                }        

### Initial flow
        self.initflow ={'mass':{"Name":"mass","amount":1000},
                        'C_cont':{"Name":"C_cont","amount":0.36,'uncertainty_type':5,'loc': 0.36 ,'minimum':0.14,'maximum':0.56},
                        'N_cont':{"Name":"N_cont","amount":0.02,'uncertainty_type':5,'loc': 0.02 ,'minimum':0.0,'maximum':0.06},
                        'P_cont':{"Name":"P_cont","amount":0.005,'uncertainty_type':5,'loc': 0.005 ,'minimum':0.0,'maximum':0.035},
                        'K_cont':{"Name":"K_cont","amount":0.014,'uncertainty_type':5,'loc': 0.014 ,'minimum':0.002,'maximum':0.040}
                        }

### Landfill
        self.Landfill ={'CH4_Collected':{"Name":"CH4_Collected","amount":70,
                                         'uncertainty_type':5,'loc': 60 ,'minimum':40,'maximum':75},
        
                        'Frac_oxidized':{"Name":"Frac_oxidized","amount":0.13,
                                         'uncertainty_type':5,'loc': 0.13 ,'minimum':0.10,'maximum':0.30},
                                         
                        'Frac_flared':{"Name":"Frac_flared","amount":0.37,
                                       'uncertainty_type':5,'loc': 0.37 ,'minimum':0.15,'maximum':0.60},
                                       
                        'percCStor_LF':{"Name":"Percent of carbon in compost remaining after 100 years","amount":80,"unit":'%'
                                        ,'uncertainty_type':5,'loc': 80 ,'minimum':40,'maximum':100}
                        }

### Monte_carlo          
    def setup_MC(self,seed=None):
        self.Compost_Input_list = {'Land_app':self.Land_app,'operation':self.operation,'Material_Properties':self.Material_Properties,
                                   'Soil_seq':self.Soil_seq,'initflow':self.initflow,'Lanfill':self.Landfill}
        super().__init__(self.Compost_Input_list)
        super().setup_MC(seed)
    
        
