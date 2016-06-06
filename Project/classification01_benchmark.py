# ----------------------------------------------------------------
# Benchmark models - CV
# ----------------------------------------------------------------

def benchmark_cv(data,fold):
    # Set K-Fold option
    kf = KFold(data.shape[0], n_folds=fold)

    # Init storage opbjects for benchmarks
    scores_benchmark01 = []
    scores_benchmark02 = []
    scores_benchmark03 = []

    # Set counter
    i = 1

    # Run cross validation
    for train, test in kf:
        
        # Trace
        trace_start(i)
        
        # Define training data set
        temp_train = data.ix[train,:]
        temp_train_data = temp_train.ix[:,1:]
        temp_train_label = temp_train.ix[:,0]

        # Define training data set
        temp_test = data.ix[test,:]
        temp_test_data = temp_test.ix[:,1:]
        temp_test_label = temp_test.ix[:,0]
        n_test = len(temp_test_label)

        # Uniform prediction
        unweighted_prediction = benchmark(temp_train_label.tolist(),n_test)
        temp_acc01 = sum(temp_test_label == unweighted_prediction) / float(n_test)
        scores_benchmark01.append(temp_acc01)

        # Weighted Prediction
        weighted_prediction = weighted_benchmark( temp_train_label.tolist(),n_test)
        temp_acc02 = sum(temp_test_label == weighted_prediction) / float(n_test)
        scores_benchmark02.append(temp_acc02)

        # First nearest neighbhor classifier
        neigh = KNeighborsClassifier(n_neighbors=1)
        neigh.fit(temp_train_data, temp_train_label) 
        firstnn_prediction = neigh.predict(temp_test_data)
        temp_acc03 = sum(temp_test_label == firstnn_prediction) / float(n_test)
        scores_benchmark03.append(temp_acc03)

        # Trace
        trace_finish(i)

        # Update counter
        i = i + 1

    # Mean Accuracy for benchmarks
    benchamrk01 = round(np.mean(scores_benchmark01),3)
    benchamrk02 = round(np.mean(scores_benchmark02),3)
    benchamrk03 = round(np.mean(scores_benchmark03),3)

    # Combine results
    results = [
                ['Uniform Sampling',benchamrk01],
                ['Weighted Sampling',benchamrk02],
                ['1NN',benchamrk03]
              ]

    return results
