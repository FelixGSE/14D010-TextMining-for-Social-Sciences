# ----------------------------------------------------------------
# Remove stuff from document
# ----------------------------------------------------------------

def full_preprocess(list_of_lyrics):
    
    processed = []
    errors = []
    for i, song in enumerate(list_of_lyrics):
        try:
            temp = preprocess( song,'[^0-9a-zA-Z]+',lower = True )
            processed.append(temp)
        except:
            errors.append(i)
    if len(errors) != 0:
        print '------------------------------'
        print "WARNING - found" + len(errors) + "erros!"
        print '------------------------------'
    
    return processed

# ----------------------------------------------------------------
# Remove stopwords
# ----------------------------------------------------------------

def remove_stopwords(list_of_tokens):
    
    stop = stopwords.words('english')
    clean = []

    for raw in list_of_tokens:

        temp = [i for i in raw if i not in stop]
        clean.append(temp)

    return clean

# ----------------------------------------------------------------
# Remove language from list of strings
# ----------------------------------------------------------------

def remove_idiom( list_of_strings, language = 'es'):

    language_removed = []
    removed_indices  = []

    for idy,string in enumerate(list_of_strings):

        trace_start(idy)

        temp_language = detect(string)

        if temp_language != language:

            language_removed.append(string)

        else:

            removed_indices.append(idy)

        trace_finish(idy)

    return [language_removed,removed_indices]


# ----------------------------------------------------------------
# Remove small words
# ----------------------------------------------------------------

def remove(list_of_tokens,length):

    removed_small = []
    for sub in list_of_tokens:

        temp = [i for i in sub if len(i) != length]
        removed_small.append(temp)

    return removed_small

# ----------------------------------------------------------------
# Remove small words
# ----------------------------------------------------------------

def pattern_remove(list_of_list,pattern):

    removed_pattern = []
    for sub in list_of_list:

        temp = [i for i in sub if i != pattern]
        removed_pattern.append(temp)

    return removed_pattern
    
# ----------------------------------------------------------------
# Stemm data
# ----------------------------------------------------------------

def stemm(list_of_tokens):

    stemmed = []

    for word in list_of_tokens: 
        
        temp = []

        for t in word:
            temp.append(PorterStemmer().stem(t))
        
        stemmed.append(temp)
    
    return stemmed

# ----------------------------------------------------------------
# TDM Matrix
# ----------------------------------------------------------------

def tdm_matrix(list_of_tokens):
    tdm = textmining.TermDocumentMatrix()
    for song in untokenize(stemmed):
        tdm.add_doc(song)
    tdm_songs = list(tdm.rows(cutoff=1))
    frame = pd.DataFrame(tdm_songs[1:])
    frame.columns = tdm_songs[0]
    return frame

# ----------------------------------------------------------------
# NGRAM Matrix
# ----------------------------------------------------------------

def ngram(list_of_strings,n):

    vectorizer = CountVectorizer(ngram_range=(n, n))
    X = vectorizer.fit_transform(list_of_strings)
    colnames = vectorizer.get_feature_names()
    ngram_matrix = X.toarray()

    frame = pd.DataFrame(ngram_matrix)
    frame.columns = colnames
    return frame

# ----------------------------------------------------------------
# TDM Matrix
# ----------------------------------------------------------------

def tf_idf(tdm,norm = "l2"):
    tfidf = TfidfTransformer(norm=norm)
    tfidf.fit(tdm)
    tf_idf_matrix = tfidf.transform(tdm).todense()
    final = pd.DataFrame(tf_idf_matrix)
    final.columns = tdm.columns
    return final


def tf_idf_feature_selection(list_of_strings,n,k):
    vectorizer = CountVectorizer(ngram_range=(n, n),max_features=k)
    X = vectorizer.fit_transform(list_of_strings)
    colnames = vectorizer.get_feature_names()
    ngram_matrix = X.toarray()
    frame = pd.DataFrame(ngram_matrix)
    frame.columns = colnames
    return frame
# ----------------------------------------------------------------
# Count unique terms
# ----------------------------------------------------------------

def unique_terms(list_of_tokens):
    unique_count = []
    for sub in list_of_tokens:
        count= len(set(sub))
        unique_count.append(count)
    return unique_count

# ----------------------------------------------------------------
# Compute length of song title
# ----------------------------------------------------------------

def token_length(list_of_tokens):
    title_len = []
    for sub in list_of_tokens:
        length = len(sub)
        title_len.append(length)
    return title_len

# ----------------------------------------------------------------
# Compute basic sentiment of the text
# ----------------------------------------------------------------

def sentiment(list_of_tokens,trace=True):
    sentiment = []
    for idx,word in enumerate(list_of_tokens): 
        if trace == True:
            trace_start(idx)
        temp_document = [str(t) for t in word]
        joined = " ".join(temp_document)
        afinn = Afinn()
        temp_score = afinn.score(joined)
        sentiment.append(temp_score)
        if trace == True:
            trace_finish(idx)
    return sentiment

# ----------------------------------------------------------------
# Wrapper for lda
# ----------------------------------------------------------------

def my_lda(list_of_tokens,topics = 2,npass=20):

    dictionary = corpora.Dictionary(list_of_tokens)    
    corpus = [dictionary.doc2bow(text) for text in list_of_tokens]

    ldamodel = gensim.models.ldamodel.LdaModel(corpus,num_topics=topics, id2word = dictionary, passes=npass)
    topic_found = ldamodel.print_topics()
    lda_prediction = process_tuples(ldamodel[corpus],topics)

    return [lda_prediction,topic_found]

# ----------------------------------------------------------------
# Find the number of topics of LDA based on likelihood
# ----------------------------------------------------------------

def find_k_lda(document_term_matrix,k=range(2,4),n=100):
    
    avg_likelihoods = []

    for idx in k:
        trace_start(idx)
        model = lda.LDA(n_topics=idx, n_iter=n, random_state=1)
        model.fit(document_term_matrix)
        temp_average = list_avg(model.loglikelihoods_)
        avg_likelihoods.append(temp_average)
        trace_finish(idx)
    index = np.argmin(avg_likelihoods)
    like_min = avg_likelihoods[index]
    best_k = k[index]
    opt_params = [best_k,like_min]
    final_output = [opt_params,avg_likelihoods]    
    return final_output

# ----------------------------------------------------------------
# Find intersection
# ----------------------------------------------------------------

def intersect(a, b):
    return list(set(a) & set(b))

# ----------------------------------------------------------------
# Find intersection
# ----------------------------------------------------------------

def remove_indices(array,list_of_indices):
    eliminate = [i for j, i in enumerate(array) if j not in list_of_indices]
    return eliminate




