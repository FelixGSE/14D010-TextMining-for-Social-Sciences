

from bs4 import BeautifulSoup
import urllib
import time 
import random
import os

html = urllib.urlopen('http://www.songlyrics.com/lady-gaga/orange-colored-sky-lyrics/').read()
soup = BeautifulSoup(html)

print soup.prettify()

print soup.find(id='songLyricsDiv')

print to_search_string("Dead and Gone")
html = urllib.urlopen('http://www.riaa.com/gold-platinum/?tab_active=default-award&se=Rihanna+We+Ride').read()
soup = BeautifulSoup(html)
print soup.prettify()

print "Platinum" and "REHAB" in soup.find('p',  class_="share_text") 

print  "Gold" and "WE RIDE" in str(soup.find('p',  class_="share_text"))
print  in str(soup)