# ----------------------------------------------------------------
# Random Forest - ADA Boost
# ----------------------------------------------------------------

def svm_cv(data,fold,kernel='rbf',C=1.0):

    # Convert data to numpies
    X = np.array(data.ix[:,1:])
    Y = np.array(data.ix[:,0])
    # Set K-Fold option
    kf = KFold(data.shape[0], n_folds=fold)

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

        clf = SVC(C=C,kernel=kernel)
        clf.fit(temp_train_data, temp_train_label)
        rf_prediction = clf.predict(temp_test_data)

        temp_acc = sum(temp_test_label == rf_prediction) / float(n_test)

        accuracies.append(temp_acc)

        # Trace
        trace_finish(i)

         # Update counter
        i = i + 1

    rfscore = round(np.mean(accuracies),3)

    return rfscore