# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 09:41:44 2019

@author: msardar2
"""
import numpy as np
import pandas as pd

### Flow
class flow:
    def __init__(self):
        self.Index = ['Compost']
        self.data = pd.DataFrame(index = self.Index,columns=['mass','sol_cont','moist_cont','vs_cont','ash_cont','C_cont','N_cont','P_cont','K_cont'])

### Create new flow
    def init_flow(self,mass,S_cont,Vol_cont,C_cont,N_cont,P_cont,K_cont):
        self.data['mass']= 1
        self.data['sol_cont'] = S_cont
        self.data['moist_cont'] = 1- S_cont
        self.data['vs_cont'] = Vol_cont
        self.data['ash_cont'] = 1- Vol_cont
        self.data['C_cont'] = C_cont
        self.data['N_cont'] = N_cont
        self.data['P_cont'] = P_cont
        self.data['K_cont'] = K_cont
###
def add_LCI(Name,Flow,LCI):
    if Name in LCI.columns:
        LCI[Name] += Flow
    else:
        LCI[Name] = Flow
            
### Apply compost to Land
def compost_use(input,CommonData,Compost_input,LCI):
    if Compost_input.operation['choice_BU']['amount'] == 1:
        # Carbon in final compost
        C_storage = input.data['C_cont'] * Compost_input.Soil_seq['perCStor']['amount']/100
        C_released = input.data['C_cont'] - C_storage
        C_storage_hummus_formation = input.data['C_cont'] * Compost_input.Soil_seq['humFormFac']['amount']
        add_LCI('Carbon dioxide, non-fossil', C_released * CommonData.MW['CO2']['amount']/CommonData.MW['C']['amount'] ,LCI)
        add_LCI('Carbon dioxide, non-fossil storage', -(C_storage+C_storage_hummus_formation) * CommonData.MW['CO2']['amount']/CommonData.MW['C']['amount'] ,LCI)
        
        #Nitrogen in final compost
        N2O = input.data['N_cont'] * Compost_input.Land_app['perN2Oevap']['amount']/100 
        NH3 = input.data['N_cont'] * Compost_input.Land_app['perNasNH3fc']['amount']/100 * Compost_input.Land_app['perNH3evap']['amount']/100
        NO3_GW = input.data['N_cont'] * CommonData.Land_app['NO3leach']['amount'] 
        FNO3_SW = input.data['N_cont'] * CommonData.Land_app['NO3runoff']['amount'] 
        
        add_LCI('Dinitrogen monoxide', N2O * CommonData.MW['Nitrous_Oxide']['amount']/CommonData.MW['N']['amount']/2 ,LCI)
        add_LCI('Ammonia',NH3 * CommonData.MW['Ammonia']['amount']/CommonData.MW['N']['amount'] ,LCI)
        add_LCI('Nitrate (ground water)',NO3_GW * CommonData.MW['Nitrate']['amount']/CommonData.MW['N']['amount'] ,LCI)
        add_LCI('Nitrate (Surface water)',FNO3_SW * CommonData.MW['Nitrate']['amount']/CommonData.MW['N']['amount'] ,LCI)
        
        
        if Compost_input.operation['fertOff']['amount'] == 1:
            # Nutrients availble in the final compost
            Navail = input.data['N_cont'] * CommonData.Land_app['MFEN']['amount'] 
            Pavail = input.data['P_cont'] * CommonData.Land_app['MFEP']['amount'] 
            Kavail = input.data['K_cont'] * CommonData.Land_app['MFEK']['amount'] 
            
            # Diesel use for applying the compost
            Diesel_use = input.data['mass'] /1000 * CommonData.Land_app['cmpLandDies']['amount']
            add_LCI(('Technosphere', 'Equipment_Diesel'), Diesel_use ,LCI)
            
            # Offset from fertilizer
            Diesel_offset = -(Navail*CommonData.Land_app['DslAppN']['amount']+Pavail*CommonData.Land_app['DslAppP']['amount']+Kavail*CommonData.Land_app['DslAppK']['amount'])
            add_LCI(('Technosphere', 'Equipment_Diesel'), Diesel_offset ,LCI)
            add_LCI(('Technosphere', 'Nitrogen_Fertilizer'), -Navail ,LCI)
            add_LCI(('Technosphere', 'Phosphorous_Fertilizer'), -Pavail ,LCI)
            add_LCI(('Technosphere', 'Potassium_Fertilizer'), -Kavail ,LCI)
            
            # offset from applying fertilizer
            Fert_N2O = -Navail * CommonData.Land_app['fert_N2O']['amount']/100 
            Fert_NH3 = -Navail * CommonData.Land_app['fert_NH3']['amount']/100 * CommonData.Land_app['fert_NH3Evap']['amount']/100
            Fert_NO3_GW = -Navail * CommonData.Land_app['fert_NO3Leach']['amount'] /100
            Fert_NO3_SW = -Navail * CommonData.Land_app['fert_NO3Run']['amount'] / 100
            
            add_LCI('Dinitrogen monoxide', Fert_N2O * CommonData.MW['Nitrous_Oxide']['amount']/CommonData.MW['N']['amount']/2 ,LCI)
            add_LCI('Ammonia',Fert_NH3 * CommonData.MW['Ammonia']['amount']/CommonData.MW['N']['amount'] ,LCI)
            add_LCI('Nitrate (ground water)',Fert_NO3_GW * CommonData.MW['Nitrate']['amount']/CommonData.MW['N']['amount'] ,LCI)
            add_LCI('Nitrate (Surface water)',Fert_NO3_SW * CommonData.MW['Nitrate']['amount']/CommonData.MW['N']['amount'] ,LCI)
                    
        if Compost_input.operation['peatOff']['amount'] == 1:
            Peat = input.data['mass']/Compost_input.Material_Properties['densFC']['amount'] * Compost_input.Land_app['densPeat']['amount'] / 1000 \
                    * Compost_input.Land_app['PeatSubFac']['amount']
            add_LCI(('Technosphere', 'Peat'), -Peat ,LCI)  
    
    if Compost_input.operation['choice_BU']['amount'] == 0:
        # Carbon in final compost
        C_storage = input.data['C_cont'] * Compost_input.Landfill['percCStor_LF']['amount']/100
        
        C_released = (input.data['C_cont'] - C_storage)/2
        C_CH4 = (input.data['C_cont'] - C_storage)/2
        C_CH4_Oxidized = C_CH4 * Compost_input.Landfill['Frac_oxidized']['amount'] * (1-Compost_input.Landfill['CH4_Collected']['amount'] /100)
        C_CH4_Flared = C_CH4 * Compost_input.Landfill['CH4_Collected']['amount'] /100 * Compost_input.Landfill['Frac_flared']['amount']
        C_CH4_Emitted = C_CH4 * (1-Compost_input.Landfill['Frac_oxidized']['amount']) * (1-Compost_input.Landfill['CH4_Collected']['amount'] /100)
        C_CH4_EnergyRec = C_CH4 * Compost_input.Landfill['CH4_Collected']['amount'] /100 * (1-Compost_input.Landfill['Frac_flared']['amount'])
        C_CH4_Electricity = C_CH4_EnergyRec*CommonData.MW['CH4']['amount']/CommonData.MW['C']['amount']*50/3.6  # LHV of Methane: 50 MJ/kg
                
        add_LCI('Carbon dioxide, non-fossil storage', -(C_storage) * CommonData.MW['CO2']['amount']/CommonData.MW['C']['amount'] ,LCI)
        add_LCI('Carbon dioxide, non-fossil', (C_released+C_CH4_EnergyRec+C_CH4_Flared+C_CH4_Oxidized) * CommonData.MW['CO2']['amount']/CommonData.MW['C']['amount'] ,LCI)
        add_LCI('Methane, non-fossil', C_CH4_Emitted * CommonData.MW['CH4']['amount']/CommonData.MW['C']['amount'] ,LCI)
        add_LCI(('Technosphere', 'Electricity_production'), C_CH4_Electricity ,LCI)
        
        #General emissions from LF
        add_LCI(('Technosphere', 'compost_to_LF'), input.data['mass'] /1000 ,LCI)
        
        #Amomonium emission from LF (Calculated base on the ammomium/N_cont ratio in LF)
        NH4_GW= 0.0051/100 * input.data['N_cont']
        NH4_SW= 0.3597/100 * input.data['N_cont']
        add_LCI('Ammonium, ion (ground water)', NH4_GW * CommonData.MW['Ammonium']['amount']/CommonData.MW['N']['amount'] ,LCI)
        add_LCI('Ammonium, ion (surface water)', NH4_SW * CommonData.MW['Ammonium']['amount']/CommonData.MW['N']['amount'] ,LCI)
 