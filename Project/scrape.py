####################################################################################################

####################################################################################################

# Load Modules
from bs4 import BeautifulSoup
import urllib
import time 
import random
import os
import re
import json

# Load external functions 
os.chdir('/Users/felix/Documents/GSE/Term 3/14D010 Text Mining for Social Sciences/14D010-TextMining-for-Social-Sciences/Project/')
execfile('wiki_scrape.py')
execfile('lyrics_scrape.py')

####################################################################################################

####################################################################################################

# Def input
wiki = 'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_'
start_year = 2000
end_year = 2015

# Get Charts from start to end 
charts = wiki_crawl(start_url = wiki, start = start_year, end = end_year , trace = True)

with open("songs.json", 'w') as songs:
    json.dump( charts[0], songs, indent = 3 )

with open("songs.json", 'w') as songs:
    json.dump( charts[1], songs, indent = 3 )

with open('songs.json') as data_file:    
    charts = json.load(data_file)

lyrics01 = crawl_lyrics(charts[0][0:499])
with open("full_songs_1.json", 'w') as songs:
    json.dump( lyrics01, songs, indent = 3 )
lyrics02 = crawl_lyrics(charts[500:1000])
with open("full_songs_2.json", 'w') as songs:
    json.dump( lyrics02, songs, indent = 3 )
lyrics03 = crawl_lyrics(charts[1001:1499])
with open("full_songs_3.json", 'w') as songs:
    json.dump( lyrics03, songs, indent = 3 )


set01 = read('full_songs_1.json')
set02 = read('full_songs_2.json')
set03 = read('full_songs_3.json')
full_set = set01 + set02 + set03


####################################################################################################

####################################################################################################

