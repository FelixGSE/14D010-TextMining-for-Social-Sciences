# Load Modules
import numpy as np
from sklearn import svm, grid_search, datasets
from sklearn.cross_validation import KFold
import pandas as pd 

# Load auxilliary functions
execfile('auxilliary_functions.py')

# Load Data
frame = pd.read_csv('frame.csv')

# Convert data to numpies
X = np.array(frame.ix[:,1:])
Y = np.array(frame.ix[:,0])

# Define parameter grid
param_grid = [
  {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
  {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
 ]

 # Initialize model and run grid search
svr = svm.SVC()
clf = grid_search.GridSearchCV(svr, param_grid)
clf.fit(X, Y)

# Subset parameters
svm_params = dic2list(clf.best_params_)

# Dump best parameter setting
save(svm_params)
