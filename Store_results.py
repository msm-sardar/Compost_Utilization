# -*- coding: utf-8 -*- 
"""
Created on Wed Aug 28 12:47:27 2019 

@author: msardar2
"""
import pandas as pd
def store_results(result,impact):
    output=pd.DataFrame()
    output[impact + ' score'] = [result[i][1] for i in range(len(result))]
    
    for j in range(len(result[0][2])):
            output[result[0][2][j][0]] = [result[i][2][j][1] for i in range(len(result))]
    
    return(output)

