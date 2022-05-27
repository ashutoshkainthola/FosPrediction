import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
import joblib

df =  pd.read_csv("Ann.csv")

X= df.loc[:, df.columns != "FOS"]
y = df["FOS"]

X= np.array(X, dtype=float)
X= np.array(X, dtype=float)


slr = LinearRegression().fit(X,y)
slr.score(X,y)

import pickle 
pickle_out = open("slr.pkl", "wb")
pickle.dump(slr, pickle_out)
pickle_out.close()
