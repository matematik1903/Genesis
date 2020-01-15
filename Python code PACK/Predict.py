import pandas as pd
x = pd.read_csv('for_predictPY.csv')

# XgBoost
import xgboost as xgb
from xgboost import Booster

# Load model
xgbost_model = xgb.XGBRegressor()
booster = Booster()
model = booster.load_model("Predict_model-version[0.1].model")
xgbost_model._Booster = booster

xgbost_predict = xgbost_model.predict(data=x)

print(xgbost_predict)
