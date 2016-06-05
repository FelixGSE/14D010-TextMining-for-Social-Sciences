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

# Load auxilliary functions
execfile('auxilliary_functions.py')

# Read Music data and combine data
s01 = read('rec01.json')
s02 = read('rec02.json')
s03 = read('rec03.json')
full_songs = s01[0] + s02[0] + s03[0] 

# Subset the last column
lyrics = column(full_songs,3)

# Step 1) Preprocess data
processed = []
errors = []
for i, song in enumerate(lyrics):
	try:
		temp = preprocess( song,'[^0-9a-zA-Z]+',lower = True )
		processed.append(temp)
	except:
		errors.append(i)

# Step 2) Remove stop words
stop = stopwords.words('english')
clean = []
for raw in processed:
	temp = [i for i in raw if i not in stop]
	clean.append(temp)

# Step 3) Stemming
stemmed = []
for word in clean: 
	temp_stemming = [str(PorterStemmer().stem(t)) for t in word]
	new_row = " ".join(temp_stemming)
	stemmed.append(new_row)

# Step 4) Compute Term Document Matrix
tdm = textmining.TermDocumentMatrix()
for song in stemmed:
	 tdm.add_doc(song)

tdm_songs = list(tdm.rows(cutoff=1))

# Step 5) Post process data
frame = pd.DataFrame(tdm_songs[1:])
frame.columns = tdm_songs[0]
frame.insert(0, 'y', column(full_songs,0))

# Compute LDA


# Compute Sentiment


# Save data frame to harddrive
frame.to_csv('frame.csv',index=False)