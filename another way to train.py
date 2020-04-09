# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 19:50:28 2020

@author: ADITYA SINGH
"""

from sklearn.utils import shuffle
df = shuffle(df, random_state=42)


X = df[[col for col in df.columns.values if col not in ['item_name', 'item_category_name', 'shop_name', 'item_cnt_month', 'item_cnt_prev_month', 'item_cnt_month_mean']]].fillna(0)

y = df['item_cnt_month'].fillna(0)


list_training = list(X['date_block_num']<33)
list_testing = list(X['date_block_num']==33)

X_train = X[X['date_block_num']<33]
y_train = y[list_training].fillna(0)
X_test= X[X['date_block_num']==33]
y_test= y[list_testing].fillna(0)


from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(X_train,y_train)

y_pred=regressor.predict(X_test)


rmse = sqrt(mean_squared_error(y_test, y_pred))

print(rmse)