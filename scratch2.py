# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:45:15 2020

@author: ADITYA SINGH
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from datetime import datetime

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

sales_train1 = sales_train.groupby(['shop_id', 'date_block_num', 'item_id', 'year', 'month'], as_index=False)['item_cnt_day'].sum().rename(columns={'item_cnt_day':'item_cnt_month'})
