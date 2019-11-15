# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:05:32 2019

@author: msardar2
"""
import pandas as pd
import numpy as np
from MC import *
class CommonData(MC):
    def __init__(self):
### Materials
        self.Index = ['Unit','Yard_Trimmings_Leaves', 'Yard_Trimmings_Grass', 'Yard_Trimmings_Branches', 'Food_Waste_Vegetable', 'Food_Waste_Non_Vegetable',
         'Wood', 'Wood_Other', 'Textiles', 'Rubber_Leather', 'Newsprint', 'Corr_Cardboard', 'Office_Paper', 'Magazines', 'third_Class_Mail',
         'Folding_Containers', 'Paper_Bags', 'Mixed_Paper', 'Paper_Non_recyclable', 'HDPE_Translucent_Containers', 'HDPE_Pigmented_Containers',
         'PET_Containers', 'Plastic_Other_1_Polypropylene', 'Plastic_Other_2', 'Mixed_Plastic', 'Plastic_Film', 'Plastic_Non_Recyclable',
         'Ferrous_Cans', 'Ferrous_Metal_Other', 'Aluminum_Cans', 'Aluminum_Foil', 'Aluminum_Other', 'Ferrous_Non_recyclable', 'Al_Non_recyclable',
         'Glass_Brown', 'Glass_Green', 'Glass_Clear', 'Mixed_Glass', 'Glass_Non_recyclable', 'Misc_Organic', 'Misc_Inorganic', 'E_waste',
         'Aerobic_Residual', 'Anaerobic_Residual', 'Bottom_Ash', 'Fly_Ash', 'Diapers_and_sanitary_products', 'Waste_Fraction_47', 'Waste_Fraction_48',
         'Waste_Fraction_49', 'Waste_Fraction_50', 'Waste_Fraction_51', 'Waste_Fraction_52', 'Waste_Fraction_53', 'Waste_Fraction_54', 'Waste_Fraction_55',
         'Waste_Fraction_56', 'Waste_Fraction_57', 'Waste_Fraction_58', 'Waste_Fraction_59', 'Waste_Fraction_60']
        
### Molecular Weights
        self.MW= {"C":{"Name":"Carbon MW","amount":12.011,"unit":"g/mol","Reference":None},
                "P":{"Name":"Phosphorus MW","amount":30.974,"unit":"g/mol","Reference":None},
                "H":{"Name":"Hydrogen MW","amount":1.008,"unit":"g/mol","Reference":None},
                "N":{"Name":"Nitrogen MW","amount":14.007,"unit":"g/mol","Reference":None},
                "O":{"Name":"Oxygen MW","amount":15.999,"unit":"g/mol","Reference":None},
                "K":{"Name":"K MW","amount":39.098,"unit":"g/mol","Reference":None},
                "S":{"Name":"S MW","amount":32.065,"unit":None,"Reference":None},
                "Cl":{"Name":"Cl MW","amount":35.453,"unit":None,"Reference":None},
                "H2":{"Name":"H2 MW","amount":2 * 1.008 ,"unit":"g/mol","Reference":None},
                "CO":{"Name":"CO MW","amount":12.011+15.999  ,"unit":"g/mol","Reference":None},
                "CO2":{"Name":"CO2 MW","amount":15.999 * 2 +12.011 ,"unit":"g/mol","Reference":None},
                "CH4":{"Name":"CH4 MW","amount":12.011 + 4 * 1.008,"unit":"g/mol","Reference":None},
                "H2O":{"Name":"H2O MW","amount":15.999 + 2 * 1.008,"unit":"g/mol","Reference":None},
                "SO2":{"Name":"SO2 MW","amount":2 * 15.999 + 32.065,"unit":"g/mol","Reference":None},
                "HCl":{"Name":"HCl MW","amount": 35.453 + 1.008 ,"unit":"g/mol","Reference":None},
                "NOx":{"Name":"HCl MW","amount": 14.007 + 2 * 15.999 ,"unit":"g/mol","Reference":None},
                "Hydrocarbons":{"Name":"Hydrocarbons MW","amount":86.18,"unit":None,"Reference":None},
                "Nitrous_Oxide":{"Name":"Nitrous_Oxide MW","amount": 2 * 14.007 + 15.999 ,"unit":None,"Reference":None},
                "Ammonia":{"Name":"Ammonia MW","amount": 14.007 + 3 * 1.008 ,"unit":None,"Reference":None},
                "Ammonium":{"Name":"Ammonium MW","amount": 14.007 + 4 * 1.008 ,"unit":None,"Reference":None},
                "Nitrate":{"Name":"Ammonia MW","amount": 14.007 + 3 * 15.999 ,"unit":None,"Reference":None}
                }      
        
### Unit Conversion
        self.UC = {'BTU_KJ':{"Name":"BTU to KJ","amount":1.055,"unit":"kJ","Reference":None},
                  'KJ_BTU':{"Name":"KJ to BTU","amount":1 / 1.055,"unit":"BTU","Reference":None}}
        
        
### STP Measurements
        self.STP = {'mole_to_L':{"Name":"mole to Liter","amount":22.41 ,"unit":"L","Reference":None},
                   'm3CH4_to_kg':{"Name":"m3 CH4 to kg CH4","amount": 0.71589 ,"unit":"kg","Reference":None},
                   'm3CO2_to_kg':{"Name":"m3 CO2 to kg","amount": self.MW['CO2']['amount']/22.41 ,"unit":"kg","Reference":None},
                   "Density_Air":{"Name":"Density_Air","amount":22.4,"unit":"L/mol","Reference":None}
                   }
        
        self.Evap_heat = {"Water_Evap_Heat":{"Name":"Water_Evap_Heat","amount":2.26,"unit":"MJ/Kg","Reference":None}}
        
### Land application inputs
        self.Land_app = {
                'cmpLandDies':{"Name":"Compost application diesel use","amount":0.8,"unit":'L/Mg compost'},
                
                'NO3runoff':{"Name":"Nitrogen runoff to surface water","amount":0.15,"unit":'kg N/kg N applied',
                             'uncertainty_type':0,'loc': 0.15 ,'scale':0.05,'minimum':0.0,'maximum':0.30},
                
                'NO3leach':{"Name":"Nitrogen leaching to ground water","amount":0.20,"unit":'kg N/kg N applied',
                            'uncertainty_type':0,'loc': 0.20 ,'scale':0.15,'minimum':0.07,'maximum':0.60},
                
                'MFEN':{"Name":"Nitrogen mineral fertilizer equivalent","amount":0.6,"unit":'kg N/kg N applied',
                        'uncertainty_type':0 ,'minimum':0.2,'maximum':0.8},
                
                'MFEP':{"Name":"Phosphorus mineral fertilizer equivalent","amount":0.9,"unit":'kg N/kg N applied',
                        'uncertainty_type':0,'minimum':0.6,'maximum':1}, 
                
                'MFEK':{"Name":"Potassium mineral fertilizer equivalent","amount":0.9,"unit":'kg N/kg N applied',
                        'uncertainty_type':0,'minimum':0.6,'maximum':1},
                
                'DslAppN':{"Name":"Fertilizer - Diesel fuel for application per kg N","amount":0.00229 ,"unit":'L/kg'},
                'DslAppP':{"Name":"Fertilizer - Diesel fuel for application per kg P","amount":0.00186 ,"unit":'L/kg'},
                'DslAppK':{"Name":"Fertilizer - Diesel fuel for application per kg K","amount":0.00125 ,"unit":'L/kg'},
                
                'fert_NO3Run':{"Name":"Fertilizer - Nitrate runoff to surface water","amount":10 ,"unit":'%',
                               'uncertainty_type':0,'loc': 10,'scale':10 ,'minimum':5,'maximum':40},
                
                'fert_NO3Leach':{"Name":"Fertilizer - Nitrate leaching to ground water","amount":10 ,"unit":'%',
                                 'uncertainty_type':0,'loc': 10,'scale':10 ,'minimum':5,'maximum':40},
                
                'fert_N2O':{"Name":"Fertilizer - N released as N2O","amount":1.8 ,"unit":'%',
                            'uncertainty_type':0,'loc': 1.8 ,'scale':0.04,'minimum':1.2,'maximum':2.5},
                
                'fert_NH3':{"Name":"Fertilizer - N as NH3","amount":25 ,"unit":'%',
                            'uncertainty_type':0,'loc': 25 ,'scale':10,'minimum':1,'maximum':50},
                
                'fert_NH3Evap':{"Name":"Fertilizer - NH3 evaporated","amount":5 ,"unit":'%',
                                'uncertainty_type':0,'loc': 5,'scale':1,'minimum':3,'maximum':7}
                        }

### Monte_carlo          
    def setup_MC(self,seed=None):
        self.CommonData_Input_list = {'Land_app':self.Land_app}
        super().__init__(self.CommonData_Input_list)
        super().setup_MC(seed)