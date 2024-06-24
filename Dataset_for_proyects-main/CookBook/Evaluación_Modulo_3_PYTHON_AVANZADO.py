# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:09:37 2021

@author: M20
"""

import os 
os.chdir("C:/Users/M20/Python/Directory")
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

SIS = "DatosAfiliadosSIS/"
path = SIS + "DatosAfiliadosSIS.csv"

Data_SIS = pd.read_csv(path, index_col=0, encoding="latin-1")


Data_SIS.head(10)

Data_SIS.info()


df = Data_SIS.copy()
df[df['EDAD']=='NO CUENTA CON DOCUMENTO DE IDENTIDAD']

df.drop([18815, 106343, 138919, 273838, 1070929, 1387239, 
         1483419, 1501184, 1643940, 1976827],axis=0, inplace = True)

df.drop([1706326, 1823164],axis=0, inplace = True)

df['EDAD'] = pd.to_numeric(df['EDAD'])


gaaa = df.EDAD.isna()


df.EDAD.isna().sum()

df[df['EDAD']=='nan']


plt.rcParams["figure.figsize"] = (15, 7.5)
plt.hist(df['EDAD'], bins = 20, rwidth=0.85)
plt.show()


df[df['SEXO']=='FEMENINO']












