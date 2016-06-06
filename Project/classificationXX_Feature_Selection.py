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

