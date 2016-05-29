

from bs4 import BeautifulSoup
import urllib
import time 
import random
import os

html = urllib.urlopen('http://www.songlyrics.com/lady-gaga/orange-colored-sky-lyrics/').read()
soup = BeautifulSoup(html)

print soup.prettify()

print soup.find(id='songLyricsDiv')