# Load Modules
import random
import os
import re
import numpy as np
import pandas as pd
import textmining
import lda
import nltk
from nltk.corpus import stopwords
from nltk import PorterStemmer
from afinn import Afinn
import json
from sklearn.feature_extraction.text import TfidfTransformer

# For N-gram
from sklearn.feature_extraction.text import CountVectorizer

# Load auxilliary functions
execfile('auxilliary_functions.py')
execfile('process_functions.py')

# Read Music data and combine data
s01 = read('rec01.json')
s02 = read('rec02.json')
s03 = read('rec03.json')
full_songs = s01[0] + s02[0] + s03[0] 

# Subset the last column
lyrics = column(full_songs,3)


processed = full_preprocess(lyrics)
clean = remove_stopwords(processed)
stemmed = stemm(clean)
test = tdm_matrix(stemmed)

frame.insert(0, 'y', column(full_songs,0))

# Compute Sentimet
sentiment_lyrics = sentiment(clean)

print list(frame.columns.values)
# Save data frame to harddrive
frame.to_csv('frame.csv',index=False)
frame = pd.read_csv('frame.csv')

# TF IDF MATRIX

test2 =tf_idf(test)




