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
# Remove small words
# ----------------------------------------------------------------

def remove(list_of_tokens,length):

    removed_small = []
    for sub in list_of_tokens:

        temp = [i for i in sub if len(i) != length]
        removed_small.append(temp)

    return removed_small

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
    X = vectorizer.fit_transform(corpus)
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
    tf_idf_matrix = tfidf.transform(tdm)
    return tf_idf_matrix

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

    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=topics, id2word = dictionary, passes=npass)

    lda_prediction = ldamodel[corpus]

    return lda_prediction
