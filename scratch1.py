# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:26:49 2020

@author: ADITYA SINGH
"""

import numpy as np
import pandas as pd

l=[]
dataset=pd.read_csv('sales_train.csv')
itemid=pd.read_csv("items.csv")
s=dataset['item_cnt_day'].sum()
x=  itemid.iloc[:, 1:3].values
for i in range(len(x)):
    print(x[i][0])
    
    
    


print (itemid)
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
l3=[]
l1.sort()

#storing in a csv file      
md={"item_id":l1}
df=pd.DataFrame(md)
df.to_csv("all_items.csv")
       

    



        


