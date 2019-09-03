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
                'densPeat':{"Name":"Density of peat","amount":200,"unit":'kg/m3',"Reference":'17'},
                'perN2Oevap':{"Name":"Percent of applied N evaporated as N2O","amount":1.5,"unit":'%',"Reference":'16'},
                'perNH3evap':{"Name":"Percent of Ammonia that evaporates","amount":15,"unit":'%',"Reference":'16'},
                'perNasNH3fc':{"Name":"Percent N that is Ammonia","amount":50,"unit":'%',"Reference":'16'},
                }  
        
### Facility Operation
        self.operation = {
                'choice_BU':{'Name':'Digestate Beneficial Use (1) or No Beneficial Use (0)','amount':1,'unit':'0/1','Referenc':None},
                'peatOff':{'Name':'Digestate Beneficial Use offsets Peat (1 - Yes; 0 - No)','amount':1,'unit':'0/1','Referenc':None},
                'fertOff':{'Name':'Digestate Beneficial Use offsets Fertilizer (1 - Yes; 0 - No)','amount':0,'unit':'0/1','Referenc':None},
                }

### Material Properties
        self.Material_Properties ={
            'mcFC':{'Name':'Finished compost moisture content','amount':0.45 ,'unit':'mass water/total mass','Referenc':None},
            'densFC':{'Name':'Density of final compost','amount':700 ,'unit':'kg/m3','Referenc':2}
            }

### Soil Sequestration
        self.Soil_seq ={
                'perCStor':{"Name":"Percent of carbon in finished compost remaining after 100 years","amount":10,"unit":'%',"Reference":'3'},
                'humFormFac':{"Name":"100 year carbon storage from humus formation","amount":0,"unit":'kg-C/kg-C in compost',"Reference":'4'}
                }        

### Initial flow
        self.initflow ={'mass':{"Name":"mass","amount":1000},
                        'sol_cont':{"Name":"sol_cont","amount":1},
                        'moist_cont':{"Name":"moist_cont","amount":1},
                        'vs_cont':{"Name":"vs_cont","amount":1},
                        'ash_cont':{"Name":"ash_cont","amount":1},
                        'C_cont':{"Name":"C_cont","amount":1},
                        'N_cont':{"Name":"N_cont","amount":1},
                        'P_cont':{"Name":"P_cont","amount":1},
                        'K_cont':{"Name":"K_cont","amount":1}}

### Landfill
        self.Landfill ={'CH4_Collected':{"Name":"CH4_Collected","amount":70},
                        'Frac_oxidized':{"Name":"Frac_oxidized","amount":0.06},
                        'Frac_flared':{"Name":"Frac_flared","amount":0.3},
                        'percCStor_LF':{"Name":"Percent of carbon in compost remaining after 100 years","amount":50,"unit":'%'}
                        }

### Monte_carlo          
    def setup_MC(self,seed=None):
        self.Compost_Input_list = {'Land_app':self.Land_app,'operation':self.operation,'Material_Properties':self.Material_Properties,'Soil_seq':self.Soil_seq}
        super().__init__(self.Compost_Input_list)
        super().setup_MC(seed)
    
        
