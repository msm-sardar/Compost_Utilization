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
                #'distLand':{"Name":"Distance to application site","amount":20,"unit":'km',"Reference":None},
                #'erLand':{"Name":"Empty return from land application (0=no; 1=yes)","amount":1,"unit":'0/1',"Reference":None},
                #'land_payload':{"Name":"Actual payload of truck used to haul soil amendment","amount":7.3,"unit":'Mg',"Reference":None},
                
                'PeatSubFac':{"Name":"Volumetric peat replacement factor","amount":0.9,"unit":None,"Reference":'17',
                              'uncertainty_type':5,'loc':0.8,'minimum':0.22,'maximum':1},
                
                'densPeat':{"Name":"Density of peat","amount":200,"unit":'kg/m3',"Reference":'17',
                            'uncertainty_type':3,'loc': 200, 'scale':57},
                
                'moistPeat':{"Name":"moistPeat","amount":0.56,"unit":None,
                            'uncertainty_type':3,'loc': 0.56, 'scale':0.05},
                
                'CContPeat':{"Name":"CContPeat","amount":0.504,"unit":None,
                            'uncertainty_type':5,'loc': 0.504,'minimum':0.48,'maximum':0.63},
                
                'CstorePeat':{"Name":"CstorePeat","amount":0.10,"unit":None,
                            'uncertainty_type':4,'minimum':0.02,'maximum':0.16},
                
                'perN2Oevap':{"Name":"Percent of applied N evaporated as N2O","amount":1.8,"unit":'%',
                              'uncertainty_type':4,'minimum':1.3,'maximum':2.2},
                
                'perNH3evap':{"Name":"Percent of Ammonia that evaporates","amount":15,"unit":'%',"Reference":'16',
                              'uncertainty_type':5,'loc':15,'minimum':10,'maximum':20},
                              
                'perNasNH3fc':{"Name":"Percent N that is Ammonia","amount":25,"unit":'%',"Reference":'16',
                               'uncertainty_type':4,'minimum':1,'maximum':50},
                }  
        
### Facility Operation
        self.operation = {
                'choice_BU':{'Name':'Digestate Beneficial Use (1) or No Beneficial Use (0)','amount':0,'unit':'0/1','Referenc':None},
                'peatOff':{'Name':'Digestate Beneficial Use offsets Peat (1 - Yes; 0 - No)','amount':1,'unit':'0/1','Referenc':None},
                'fertOff':{'Name':'Digestate Beneficial Use offsets Fertilizer (1 - Yes; 0 - No)','amount':0,'unit':'0/1','Referenc':None},
                'allocation_ADC':{'Name':'Allocation factor of LF material use to ADC','amount':0.5,'unit':'frac',
                                  'uncertainty_type':4,'minimum':0,'maximum':1}}

### Material Properties
        self.Material_Properties ={
            'mcFC':{'Name':'Finished compost moisture content','amount':0.45 ,'unit':'mass water/total mass','Referenc':None,
                    'uncertainty_type':4,'minimum':0.18,'maximum':0.67},
            'densFC':{'Name':'Density of final compost','amount':700 ,'unit':'kg/m3','Referenc':2,
                      'uncertainty_type':3,'loc': 700 ,'scale':110}
            }

### Soil Sequestration
        self.Soil_seq ={
                'perCStor':{"Name":"Percent of carbon in finished compost remaining after 100 years","amount":10,"unit":'%'
                            ,'uncertainty_type':4,'minimum':2,'maximum':16},
                'humFormFac':{"Name":"100 year carbon storage from humus formation","amount":0,"unit":'kg-C/kg-C in compost',"Reference":'4'}
                }        

### Initial flow
        self.initflow ={'mass':{"Name":"mass","amount":1000},
                        'C_cont':{"Name":"C_cont","amount":0.30,'uncertainty_type':4,'minimum':0.10,'maximum':0.47},
                        'N_cont':{"Name":"N_cont","amount":0.015,'uncertainty_type':4,'minimum':0.0051,'maximum':0.028},
                        'P_cont':{"Name":"P_cont","amount":0.005,'uncertainty_type':4,'minimum':0.0015,'maximum':0.0093},
                        'K_cont':{"Name":"K_cont","amount":0.01,'uncertainty_type':4,'minimum':0.0007,'maximum':0.023}
                        }

### Landfill
        self.Landfill ={'CH4_Collected':{"Name":"CH4_Collected","amount":60,
                                         'uncertainty_type':3,'loc': 60 ,'scale':4},
        
                        'Frac_oxidized':{"Name":"Frac_oxidized","amount":0.17,
                                         'uncertainty_type':3,'loc': 0.17,'scale':0.03},
                                         
                        'Frac_flared':{"Name":"Frac_flared","amount":0.31,
                                       'uncertainty_type':3,'loc': 0.31 , 'scale':0.12},
                                       
                        'percCStor_LF':{"Name":"Percent of carbon in compost remaining after 100 years","amount":90,"unit":'%'
                                        ,'uncertainty_type':3,'loc':90,'scale':3},
                                        
                        'Elec_eff':{"Name":"Elec_eff in LF","amount":0.30,"unit":None
                                        ,'uncertainty_type':4,'minimum':0.20,'maximum':0.37},
                                    
                        'CH4_LHV':{"Name":"CH4_LHV","amount":50,"unit":'MJ/kg'},
                        
                        'frac_CH4':{"Name":"frac_CH4 in biogas produced in LF","amount":0.5,"unit":None
                                        ,'uncertainty_type':4,'minimum':0.45,'maximum':0.55},
                        
                        'DC_subs_fac':{'Name':'DC_subs_fac','amount':0.9,'unit':'frac',
                                       'uncertainty_type':4,'minimum':0,'maximum':1},
                       
                        'Soil_dens':{'Name':'Soil_dens','amount':1600,'unit':'kg/m3',
                                      'uncertainty_type':5,'loc': 1600 ,'minimum':1400,'maximum':1800},
                                     
                        'DC_thickness':{'Name':'DC_thickness','amount':15,'unit':'cm',
                                        'uncertainty_type':2,'loc': 2.7081, 'scale':0.0245},
                        
                        'ADC_thickness':{'Name':'ADC_thickness','amount':22.5,'unit':'cm',
                                         'uncertainty_type':2,'loc': 3.2189, 'scale':0.1150},
                        
                        'Frac_NH4_GW':{'Name':'Frac_NH4_GW','amount':0.000048,'unit':'fraction',
                                         'uncertainty_type':2,'loc': -9.9466, 'scale':0.2093},
                        
                        'Frac_NH4_SW':{'Name':'Frac_NH4_SW','amount':0.000087,'unit':'fraction',
                                         'uncertainty_type':2,'loc': -9.3552, 'scale':0.2093},
                        }

### Monte_carlo          
    def setup_MC(self,seed=None):
        self.Compost_Input_list = {'Land_app':self.Land_app,'operation':self.operation,'Material_Properties':self.Material_Properties,
                                  'Soil_seq':self.Soil_seq,'initflow':self.initflow,'Lanfill':self.Landfill}
        super().__init__(self.Compost_Input_list)
        super().setup_MC(seed)
    
        
