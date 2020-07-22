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
                
                'PeatSubFac':{"Name":"Volumetric peat replacement factor","amount":0.9,"unit":None,"Reference":'17'},
                
                'densPeat':{"Name":"Density of peat","amount":200,"unit":'kg/m3',"Reference":'17'},
                
                'moistPeat':{"Name":"moistPeat","amount":0.56,"unit":None},
                
                'CContPeat':{"Name":"CContPeat","amount":0.504,"unit":None},
                
                'CstorePeat':{"Name":"CstorePeat","amount":0.10,"unit":None},
                
                'perN2Oevap':{"Name":"Percent of applied N evaporated as N2O","amount":1.8,"unit":'%'},
                
                'perNH3evap':{"Name":"Percent of Ammonia that evaporates","amount":15,"unit":'%',"Reference":'16'},
                              
                'perNasNH3fc':{"Name":"Percent N that is Ammonia","amount":25,"unit":'%',"Reference":'16','list':np.linspace(1,50,10).tolist()*10},
                }  
        
### Facility Operation
        self.operation = {
                'choice_BU':{'Name':'Digestate Beneficial Use (1) or No Beneficial Use (0)','amount':1,'unit':'0/1','Referenc':None},
                'peatOff':{'Name':'Digestate Beneficial Use offsets Peat (1 - Yes; 0 - No)','amount':1,'unit':'0/1','Referenc':None},
                'fertOff':{'Name':'Digestate Beneficial Use offsets Fertilizer (1 - Yes; 0 - No)','amount':1,'unit':'0/1','Referenc':None},
                'allocation_ADC':{'Name':'Allocation factor of LF material use to ADC','amount':0.5,'unit':'frac'}}

### Material Properties
        self.Material_Properties ={
            'mcFC':{'Name':'Finished compost moisture content','amount':0.45 ,'unit':'mass water/total mass','Referenc':None},
            'densFC':{'Name':'Density of final compost','amount':700 ,'unit':'kg/m3','Referenc':2}
            }

### Soil Sequestration
        self.Soil_seq ={
                'perCStor':{"Name":"Percent of carbon in finished compost remaining after 100 years","amount":10,"unit":'%'},
                'humFormFac':{"Name":"100 year carbon storage from humus formation","amount":0,"unit":'kg-C/kg-C in compost',"Reference":'4'}
                }        

### Initial flow
        self.initflow ={'mass':{"Name":"mass","amount":1000},
                        'C_cont':{"Name":"C_cont","amount":0.30},
                        'N_cont':{"Name":"N_cont","amount":0.015,'list':np.repeat(np.linspace(0.0051,0.028,10),10)},
                        'P_cont':{"Name":"P_cont","amount":0.005},
                        'K_cont':{"Name":"K_cont","amount":0.01}
                        }

### Landfill
        self.Landfill ={'CH4_Collected':{"Name":"CH4_Collected","amount":60},
        
                        'Frac_oxidized':{"Name":"Frac_oxidized","amount":0.17},
                                         
                        'Frac_flared':{"Name":"Frac_flared","amount":0.31},
                                       
                        'percCStor_LF':{"Name":"Percent of carbon in compost remaining after 100 years","amount":90,"unit":'%'},
                                        
                        'Elec_eff':{"Name":"Elec_eff in LF","amount":0.30,"unit":None},
                                    
                        'CH4_LHV':{"Name":"CH4_LHV","amount":50,"unit":'MJ/kg'},
                        
                        'frac_CH4':{"Name":"frac_CH4 in biogas produced in LF","amount":0.5,"unit":None},
                        
                        'DC_subs_fac':{'Name':'DC_subs_fac','amount':0.9,'unit':'frac'},
                       
                        'Soil_dens':{'Name':'Soil_dens','amount':1600,'unit':'kg/m3'},
                                     
                        'DC_thickness':{'Name':'DC_thickness','amount':15,'unit':'cm'},
                        
                        'ADC_thickness':{'Name':'ADC_thickness','amount':22.5,'unit':'cm'},  
                        
                        'Frac_NH4_GW':{'Name':'Frac_NH4_GW','amount':0.000054,'unit':'fraction'},
                        
                        'Frac_NH4_SW':{'Name':'Frac_NH4_SW','amount':0.000097,'unit':'fraction'}
                        
                        }

### Monte_carlo          
    def setup_MC(self,seed=None):
        self.Compost_Input_list = {'Land_app':self.Land_app,'operation':self.operation,'Material_Properties':self.Material_Properties,
                                  'Soil_seq':self.Soil_seq,'initflow':self.initflow,'Lanfill':self.Landfill}
        super().__init__(self.Compost_Input_list)
        super().setup_MC(seed)
    
        
