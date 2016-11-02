# ----------------------------------------------------------------
# CHI-Squared - Kbest
# ----------------------------------------------------------------

def chi2_kbest(data,k):

    # Subset data
    X = np.array(data.ix[:,1:])
    Y = np.array(data.ix[:,0])

    # Compute reduced data frame
    reduced = SelectKBest(chi2, k=k).fit_transform(X, Y)

    # Return data
    return reduced

# ----------------------------------------------------------------
# CHI-Squared - FDR
# ----------------------------------------------------------------

def chi2_fdr(data,alpha):

    # Subset data
    X = np.array(data.ix[:,1:])
    Y = np.array(data.ix[:,0])
    
    reduced = SelectFdr(chi2, alpha=alpha).fit_transform(X, Y)

    return reduced

# ----------------------------------------------------------------
# TF-IDF Feature selection
# ----------------------------------------------------------------

def tf_idf_feature_selection(list_of_strings,n,k):
    vectorizer = CountVectorizer(ngram_range=(n, n),max_features=k)
    X = vectorizer.fit_transform(list_of_strings)
    colnames = vectorizer.get_feature_names()
    ngram_matrix = X.toarray()
    frame = pd.DataFrame(ngram_matrix)
    frame.columns = colnames
    return frame

# ----------------------------------------------------------------
# Random Forest Feature Selection
# ----------------------------------------------------------------

def rf_feature_selection(data,k,n=1000):
    
    X = np.array(frame.ix[:,1:])
    Y = np.array(frame.ix[:,0])

    rf = RandomForestClassifier(n_estimators=n)
    rf.fit(X, y)
    feature_ranking = sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names), reverse=True)
    k_select = subset_tuples(feature_ranking,k)
    new_features = data.loc[:,k_select]

    return new_features