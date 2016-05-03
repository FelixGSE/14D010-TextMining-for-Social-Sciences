import re
import math
import numpy as np
from collections import Counter
from collections import defaultdict

class Corpus():
    
    """ 
    The Corpus class represents a document collection
     
    """
    # We added in the initialization the dictionary with respect to which you want to compute the ranking: 
    # numb is for the number of top documents you want to consider, while metric == "tfidf" or "doc-term"
    def __init__(self, doc_data, stopword_file, clean_length, pres_parties):
        
        #get a list of stopwords
        self.create_stopwords(stopword_file, clean_length)
                
        #Initialise documents by invoking the appropriate class
        self.docs = []
        for doc in doc_data:
            pres_last_name = doc[1]
            party = pres_parties[pres_last_name] if pres_last_name in pres_parties.keys() else None
            new_doc = Document(doc[0], pres_last_name, party, doc[2], self.stopwords, clean_length)
            self.docs.append(new_doc)
            
        # sort docs by political party
        groups = defaultdict(list)
        for obj in self.docs:
            groups[obj.party].append(obj)
        new_list = groups.values()
        self.docs = [item for sublist in new_list for item in sublist]
                
        self.N = len(self.docs)
        self.clean_length = clean_length
        
        #stopword removal, token cleaning and stemming to docs
        self.clean_docs(2)
        
        #create vocabulary
        self.corpus_tokens()
        
        
    def clean_docs(self, length):
        """ 
        Applies stopword removal, token cleaning and stemming to docs
        """
        for doc in self.docs:
            doc.token_clean(length)
            doc.stopword_remove(self.stopwords)
            doc.stem()        
    
    def create_stopwords(self, stopword_file, length):
        """
        description: parses a file of stowords, removes words of length < 'length' and 
        stems it
        input: length: cutoff length for words
               stopword_file: stopwords file to parse
        """
        
        with codecs.open(stopword_file,'r','utf-8') as f: raw = f.read()
        
        self.stopwords = (np.array([PorterStemmer().stem(word) 
                                    for word in list(raw.splitlines()) if len(word) > length]))
        
     
    def corpus_tokens(self):
        """
        description: create a set of all tokens or in other words a vocabulary
        """
        
        #initialise an empty set
        self.token_set = set()
        for doc in self.docs:
            self.token_set = self.token_set.union(doc.tokens) 

    def generate_document_term_matrix(self):
        """
        description: create the document_term_matrix
        """
        dimD = self.N
        # total number of columns
        dimV = len(self.token_set)
        terms_list = list(self.token_set)
        # initialize the matrix
        document_term_matrix = np.zeros((dimD, dimV))        
        for i in range(dimD):
            # count the terms for each document
            document = self.docs[i]
            if i%25==0: print 'counting terms for doc: ' + str(i)
            word_counts = Counter(document.tokens)
            for word_count_pair in word_counts.most_common():
                # split in word and count
                word = word_count_pair[0]
                count = word_count_pair[1]
                # save the term index
                term_idx = terms_list.index(word)
                doc_term_tuple = (i, term_idx)
                document_term_matrix.itemset(doc_term_tuple, count)
        # update the doc_term_matrix attribute        
        self.document_term_matrix = document_term_matrix

    def generate_idfv(self):
        """
        computes the inverse document frequency of each term v
        """
        D = self.N
        # idf_{v} = log(D/d_fv)
        terms_list = list(self.token_set)
        self.idfv = dict.fromkeys(terms_list, 0)
        # creates a hash {'term':0,'term2':0,...}
        for v in self.token_set:
            term_idx = terms_list.index(v)
            d_fv = np.sum(self.document_term_matrix[:,term_idx] > 0)
            # apply the formula
            c = math.log10(D/d_fv)
            self.idfv[v] = c

    def generate_tf_idf(self):
        D = self.N
        terms_list = list(self.token_set)
        # initialize the matrix
        tf_idf = np.zeros(self.document_term_matrix.shape)
        for doc_i in range(D):
            if doc_i%25==0: print 'counting terms for doc: ' + str(doc_i)
            for v_i in range(len(terms_list)):
                doc_term_tuple = (doc_i, v_i)
                xdv_score = self.document_term_matrix.item(doc_term_tuple)
                if xdv_score > 0:
                    idf_score = self.idfv[terms_list[v_i]]
                    if idf_score > 0:
                        # apply the formula seen in class
                        tf_idf_score = (1 + np.log(xdv_score))*idf_score
                        tf_idf.itemset(doc_term_tuple, tf_idf_score)
        self.tf_idf = tf_idf

    def dict_rank(self, numb, dictionary, metric):
        """
        computes the dictionary rank of the top numb documents, based on the dictionary and metric method 
        (either doc-term or tfidf)
        """
        terms_list = list(self.token_set)
        # get the indices of occurences of the terms in the dictionary
        idcs = [terms_list.index(item) for item in dictionary]
        order = []
        if metric == 'doc-term':
            # get the needed columns
            cols = tuple([list(self.document_term_matrix[:,i]) for i in idcs])
            # sort and update order list
            order = list(np.lexsort(cols))
            order.reverse()
        elif metric == 'tf_idf':
            cols = tuple([list(self.tf_idf[:,i]) for i in idcs])
            order = list(np.lexsort(cols))
            order.reverse()
        # return the top numb documents    
        return [self.docs[i] for i in order[0:numb]]
