# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('clev.csv')



X = dataset.iloc[:, :13]
print(X)



y = dataset.iloc[:, -1]
print(y)


from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators = 1000, random_state = 2)
rf.fit(X,y)
# Saving model to disk
pickle.dump(rf, open('model.pkl','wb'))
# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[57, 0, 0, 140, 241, 0, 1, 123, 1, 0.2, 1,0,3]]))

