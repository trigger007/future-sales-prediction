# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 01:09:52 2020

@author: Shreyansh Satvik
"""

import numpy as np
import pandas as pd
import tensorflow as tf

train=pd.read_csv('sales_train.csv')
df = pd.read_csv("sales_train.csv", parse_dates =["date"], index_col ="date")
X=df.iloc[:,:-1].values
y=df.iloc[:,4].values
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.02,random_state=0)
from sklearn.tree import DecisionTreeRegressor as regressor

  