# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:54:25 2020

@author: Tijesunimi.Adebiyi
"""

import pandas as pd
import os


myexcel = pd.ExcelFile('Data pandas.xlsx')
dataframes = []
sheets = myexcel.sheet_names

#create 'Sheets' folder
cwdpath = os.getcwd()
subfolder = 'Sheets'
path = os.path.join(cwdpath, subfolder) 

os.mkdir(path)
    

for x in range(len(sheets)):
    df = pd.read_excel(myexcel,sheets[x])
    df.to_csv('Sheets//'+sheets[x]+'.csv'
                         ,encoding='utf-8', index=False)