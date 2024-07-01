import pandas as pd
from joblib import dump
from sklearn import svm

# Global
x = pd.read_csv('py-shiny/bananas.csv')

# Train SVM
x.loc[x.ripeness == 'Under', 'target'] = 0
x.loc[x.ripeness == 'Ripe', 'target'] = 1
x.loc[x.ripeness == 'Very', 'target'] = 2
x.loc[x.ripeness == 'Over', 'target'] = 3
data_X = x[['green', 'yellow', 'brown']].to_numpy()
data_y = x.target.values
svm_model = svm.SVC(probability = True)
svm_model.fit(data_X, data_y)

#' Predict ripeness class
svm_model.predict_proba([[1, 0, 0]])
svm_model.predict_proba([[0, 1, 0]])
svm_model.predict_proba([[0, 0, 1]])
svm_model.predict_proba([[0.1, 0.2, 0.7]])

# Write model object to file
dump(svm_model, 'py-shiny/bananas-svm.joblib')
