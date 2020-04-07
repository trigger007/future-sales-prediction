# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:26:49 2020

@author: ADITYA SINGH
"""

import numpy as np
import pandas as pd

l=[]
dataset=pd.read_csv("sales_train.csv")
s=dataset['item_cnt_day'].sum()

#date manipulation
for i in range(len(dataset)):
    l.append(dataset['date'][i])
print(l[10])
print(s)
print(dataset['date'][10].split(".")[1][0]+str(3))

#all item id in a list
l1=[]
for i in range(len(dataset)):
    if dataset['item_id'][i] not in l1:
        l1.append(dataset['item_id'][i])
       
for i in range(len(dataset)):
    print(dataset['item_id'][i])
    



        


