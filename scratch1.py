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
print(dataset['date'][10].split(".")[1])

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

#
l4=[]
l5=[]
l6=[]
l7=[]
t=''

for k in range(13,16):
    for j in range(1,13):
        l4=[]
        t=str(j)+'.'+str(k)
        l4.append(t)
        for i in range(22170):
            sm=0
                for m in range(len(dataset)):
                    if dataset['item_id'][m]==i and int(dataset['date'][m].split(".")[1])==j and int(dataset['date'][m].split(".")[2])==k:
                        sm=sm+dataset['item_cnt_day'][m]
                l5=[]
                l5.append(i)
                l5.append(sm)
                l4.append(l5)
    l6.append(l4)

print("hello")       



    



        


