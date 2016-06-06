# Load Modules
import os
import json
import numpy  as np
import pandas as pd 
from sklearn import svm, grid_search, datasets
from sklearn.cross_validation  import KFold
from sklearn.feature_selection import chi2, SelectFdr,SelectKBest
from sklearn.feature_selection import 
from sklearn.neighbors   import KNeighborsClassifier
from sklearn.ensemble    import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors.nearest_centroid import NearestCentroid

# Load functions
execfile('auxilliary_functions.py')
execfile('classification01_benchmark.py')
execfile('classification03_RF.py')
execfile('classification04_NB.py')
execfile('classification05_NC.py')
execfile('classification06_KNN.py')


# Load Data
frame = pd.read_csv('frame.csv')








