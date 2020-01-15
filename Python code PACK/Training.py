# import libraries
# 1. standart
import pandas as pd
import numpy as np

# 2. for data split
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

# XgBoost
import xgboost as xgb
from sklearn import model_selection, preprocessing
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

""" 
Pre-start for learning
"""

# Read data
data_x = pd.read_csv('train_data_x.csv')
data_y = pd.read_csv('train_data_y.csv')

# Preprocessing date
data_y = data_y.drop("Unnamed: 0", axis = 1)
data_x = pd.merge(data_y, data_x,  on=['source','date', 'profit_0_day'], how='right')
data_x = data_x.drop('Unnamed: 0', axis = 1)
data_x = data_x.drop('profit_4-7', axis = 1)
data_x = data_x.fillna(0)
data_x = data_x.drop('date', axis = 1)
data_x = data_x.drop('source', axis = 1)
x = data_x
y = data_y['profit_4-7']

# split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15)

print ("Shape train part: ", x_train.shape, y_train.shape)
print ("Shape test part: ",x_test.shape, y_test.shape)

#Fitting XGB regressor
#Predict

xgbost_model = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 10, alpha = 10, n_estimators = 10)
xgbost_model.fit(x, y)

xgbost_model.save_model('Predict_model-version[0.1].model')

x_test.to_csv('for_predictPY.csv')


