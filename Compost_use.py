# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:37:26 2019

@author: msardar2
"""
import numpy as np
import pandas as pd
from Compost_input import *
from CommonData import *
from stats_arrays import *
from flow import *

class Compost_use:
    def __init__(self):
        self.CommonData = CommonData()
        self.Compost_input= Compost_input()
### Read Material properties
        self.Material_Properties=pd.read_excel("Material properties.xlsx",index_col = 'Materials')
        self.Material_Properties.fillna(0,inplace=True)
        self.Index = ['Compost']
        
### Mass Flows
    def calc(self):
        self.LCI = pd.DataFrame(index = self.Index)
### Initial mass 
        self.Compost = flow()
        self.Compost.init_flow(self.Compost_input.initflow['mass']['amount'],self.Compost_input.initflow['sol_cont']['amount'],
                               self.Compost_input.initflow['vs_cont']['amount'],self.Compost_input.initflow['C_cont']['amount'],
                               self.Compost_input.initflow['N_cont']['amount'],self.Compost_input.initflow['P_cont']['amount'],
                               self.Compost_input.initflow['K_cont']['amount'])
        
### Compost use
        compost_use(self.Compost,self.CommonData,self.Compost_input,self.LCI)
### Transportation Compost
        add_LCI('Full_Medium-duty truck transport of compost to land application', self.Compost.data['mass'] * self.Compost_input.Land_app['distLand']['amount'] ,self.LCI)
        add_LCI('Empty_Medium-duty truck transport return from land application', self.Compost.data['mass']/1000 / self.Compost_input.Land_app['land_payload']['amount']* self.Compost_input.Land_app['distLand']['amount'] ,self.LCI)

    def setup_MC(self,seed=None):
        self.Compost_input.setup_MC(seed)
    
    def MC_calc(self):      
        input_list = self.Compost_input.gen_MC()
        self.calc()
        return(input_list)
        
    def report(self):
### Output
        self.Compost_use = {}
        Waste={}
        Technosphere={}
        Biosphere={}
        self.Compost_use ["process name"] = 'Compost_use'
        self.Compost_use  ["Waste"] = Waste
        self.Compost_use  ["Technosphere"] = Technosphere
        self.Compost_use  ["Biosphere"] = Biosphere
        
        for x in [Waste,Technosphere, Biosphere]:
            for y in self.Index:
                x[y]={}
                                                       
               
        for y in self.Index:
### Output Technospphere Database
            Technosphere[y][('Technosphere', 'Internal_Process_Transportation_Medium_Duty_Diesel_Truck')] = self.LCI['Full_Medium-duty truck transport of compost to land application'] [y]
            Technosphere[y][('Technosphere', 'Empty_Return_Medium_Duty_Diesel_Truck')] = self.LCI['Empty_Medium-duty truck transport return from land application'][y]
            
            if self.Compost_input.operation['fertOff']['amount'] == 1 and self.Compost_input.operation['choice_BU']['amount'] == 1:
                Technosphere[y][('Technosphere', 'Equipment_Diesel')] = self.LCI[('Technosphere', 'Equipment_Diesel')][y]
                Technosphere[y][('Technosphere', 'Nitrogen_Fertilizer')] = self.LCI[('Technosphere', 'Nitrogen_Fertilizer')][y]
                Technosphere[y][('Technosphere', 'Phosphorous_Fertilizer')] = self.LCI[('Technosphere', 'Phosphorous_Fertilizer')][y]
                Technosphere[y][('Technosphere', 'Potassium_Fertilizer')] = self.LCI[('Technosphere', 'Potassium_Fertilizer')][y]
            else:
                Technosphere[y][('Technosphere', 'Equipment_Diesel')] = 0
                Technosphere[y][('Technosphere', 'Nitrogen_Fertilizer')] = 0
                Technosphere[y][('Technosphere', 'Phosphorous_Fertilizer')] = 0
                Technosphere[y][('Technosphere', 'Potassium_Fertilizer')] = 0
            
            if self.Compost_input.operation['peatOff']['amount'] == 1 and self.Compost_input.operation['choice_BU']['amount'] == 1:
                Technosphere[y][('Technosphere', 'Peat')] = self.LCI[('Technosphere', 'Peat')][y]
            else:
                Technosphere[y][('Technosphere', 'Peat')] = 0
            
            if self.Compost_input.operation['choice_BU']['amount'] == 0:
                Technosphere[y][('Technosphere', 'compost_to_LF')] = self.LCI[('Technosphere', 'compost_to_LF')][y]
                Technosphere[y][('Technosphere', 'Electricity_production')] = self.LCI[('Technosphere', 'Electricity_production')][y]
            else:
                Technosphere[y][('Technosphere', 'compost_to_LF')] = 0
                Technosphere[y][('Technosphere', 'Electricity_production')] = 0
            
### Output Biosphere Database

            Biosphere[y][('biosphere3', 'e4e9febc-07c1-403d-8d3a-6707bb4d96e6')]= self.LCI['Carbon dioxide, non-fossil storage'][y]# Carbon dioxide, from soil or biomass stock ('air',)
            Biosphere[y][('biosphere3', 'eba59fd6-f37e-41dc-9ca3-c7ea22d602c7')]= self.LCI['Carbon dioxide, non-fossil'][y] # Carbon dioxide, non-fossil ('air',)

            if self.Compost_input.operation['choice_BU']['amount'] == 1:
                Biosphere[y][('biosphere3', '87883a4e-1e3e-4c9d-90c0-f1bea36f8014')]= self.LCI['Ammonia'][y] #Ammonia ('air',)
                Biosphere[y][('biosphere3', '20185046-64bb-4c09-a8e7-e8a9e144ca98')]= self.LCI['Dinitrogen monoxide'][y] # Dinitrogen monoxide ('air',)
                Biosphere[y][('biosphere3', 'b9291c72-4b1d-4275-8068-4c707dc3ce33')]= self.LCI['Nitrate (ground water)'][y] #Nitrate ('water', 'ground-')
                Biosphere[y][('biosphere3', '7ce56135-2ca5-4fba-ad52-d62a34bfeb35')]= self.LCI['Nitrate (Surface water)'][y] #Nitrate ('water', 'surface water')
            else:
                Biosphere[y][('biosphere3', '87883a4e-1e3e-4c9d-90c0-f1bea36f8014')]= 0 #Ammonia ('air',)
                Biosphere[y][('biosphere3', '20185046-64bb-4c09-a8e7-e8a9e144ca98')]= 0 # Dinitrogen monoxide ('air',)
                Biosphere[y][('biosphere3', 'b9291c72-4b1d-4275-8068-4c707dc3ce33')]= 0 #Nitrate ('water', 'ground-')
                Biosphere[y][('biosphere3', '7ce56135-2ca5-4fba-ad52-d62a34bfeb35')]= 0 #Nitrate ('water', 'surface water')



            if self.Compost_input.operation['choice_BU']['amount'] == 0:
                Biosphere[y][('biosphere3', 'da1157e2-7593-4dfd-80dd-a3449b37a4d8')]= self.LCI['Methane, non-fossil'][y]
                Biosphere[y][('biosphere3', '736f52e8-9703-4076-8909-7ae80a7f8005')]= self.LCI['Ammonium, ion (ground water)'][y] #'Ammonium, ion' (kilogram, None, ('water', 'ground-'))
                Biosphere[y][('biosphere3', '13331e67-6006-48c4-bdb4-340c12010036')]= self.LCI['Ammonium, ion (surface water)'][y] # 'Ammonium, ion' (kilogram, None, ('water', 'surface water'))  
            else:
                Biosphere[y][('biosphere3', 'da1157e2-7593-4dfd-80dd-a3449b37a4d8')]= 0
                Biosphere[y][('biosphere3', '736f52e8-9703-4076-8909-7ae80a7f8005')]= 0 #'Ammonium, ion' (kilogram, None, ('water', 'ground-'))
                Biosphere[y][('biosphere3', '13331e67-6006-48c4-bdb4-340c12010036')]= 0 # 'Ammonium, ion' (kilogram, None, ('water', 'surface water'))  
     
        
        return(self.Compost_use )    



A=Compost_use()
A.calc()
A.report()

"""
A=AD()
A.calc()
AA=A.report()
AAA=A.LCI

from time import time
B = time()
A=AD()
for i in range(100):
    A.calc() 
    A.report()
print(time()-B)
"""
