# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:11:02 2020

@author: Shreyansh Satvik
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:07:36 2020

@author: Shreyansh Satvik
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt

item_cat = pd.read_csv('item_categories.csv')
items = pd.read_csv('items.csv')
sales_train = pd.read_csv('sales_train.csv')
test = pd.read_csv('test.csv')
shops = pd.read_csv('shops.csv')

#data wrangling
items = pd.merge(items, item_cat, how='left', on=['item_category_id'])

#TfidfVectorizer is used to convert text data into matrix of count tokens and is based on the no of appearences of each word.
feature_cnt = 25#25 words in a sentence (max no)
tfidf = TfidfVectorizer(max_features=feature_cnt)
item_name = pd.DataFrame(tfidf.fit_transform(items['item_name']).toarray())

def merge_dataframe(df_left, df_right, column_name_prefix):
    for column in df_right.columns.values:
        col = column_name_prefix + str(column)
        df_left[col] = df_right[column]
        
merge_dataframe(items, item_name, 'item_name')

feature_cnt = 25
tfidf = TfidfVectorizer(max_features=feature_cnt)
item_cat_name = pd.DataFrame(tfidf.fit_transform(items['item_category_name']).toarray())

merge_dataframe(items, item_cat_name, 'item_cat_name')

tfidf = TfidfVectorizer(max_features=feature_cnt)
shop_name = pd.DataFrame(tfidf.fit_transform(shops['shop_name']).toarray())

merge_dataframe(shops, shop_name, 'shop_name')
sales_train = sales_train[(sales_train['item_price']>0) & (sales_train['item_cnt_day']>0)]

item_price_latest = sales_train.sort_values(by=['date'], ascending=False).groupby(['item_id', 'shop_id'], as_index=False)['item_price'].first()#.rename(columns={'item_price': 'item_price'})

sales_train['date'] = sales_train['date'].apply(lambda x: datetime.strptime(x, '%d.%m.%Y'))
sales_train['year'] = sales_train['date'].apply(lambda x: x.year)
sales_train['month'] = sales_train['date'].apply(lambda x: x.month)

df = sales_train.groupby(['shop_id', 'date_block_num', 'item_id', 'year', 'month'], as_index=False)['item_cnt_day'].sum().rename(columns={'item_cnt_day':'item_cnt_month'})

######data preprocessing done##################
####applying random forest tree regression algorithm to this###########
X=df.iloc[:,:-1].values
y=df.iloc[:,5].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.02, random_state = 0)

from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=300,random_state=0)
regressor.fit(X_train,y_train)

y_pred=regressor.predict(X_test)


rmse = sqrt(mean_squared_error(y_test, y_pred))

print(rmse)
