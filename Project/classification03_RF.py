# Load Modules
import os
import numpy as np
from sklearn.cross_validation import KFold
from sklearn.ensemble import RandomForestClassifier
import pandas as pd 


# Load auxilliary functions
execfile('auxilliary_functions.py')

# Load Data
frame = pd.read_csv('frame.csv')

# Convert data to numpies
X = np.array(frame.ix[:,1:])
Y = np.array(frame.ix[:,0])

# Set K-Fold option
kf = KFold(frame.shape[0], n_folds=5)

# Storage list for accuracies
accuracies = []

# Set counter
i = 1

for train, test in kf:

    # Trace
    trace_start(i)

    # Define training data set
    temp_train_data = X[train,:]
    temp_train_label = Y[train]

    # Define training data set
    temp_test_data = X[test,:]
    temp_test_label = Y[test]
    
    # Size of test set
    n_test = len(temp_test_label)

    clf = RandomForestClassifier(n_estimators=1000)
    clf = clf.fit(temp_train_data, temp_train_label)
    rf_prediction = clf.predict(temp_test_data)

    temp_acc = sum(temp_test_label == rf_prediction) / float(n_test)

    accuracies.append(temp_acc)

    # Trace
    trace_finish(i)

     # Update counter
    i = i + 1

rfscore = round(np.mean(accuracies),3)

save('rfscore.json',rfscore)