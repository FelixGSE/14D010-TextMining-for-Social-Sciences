from bs4 import BeautifulSoup
import urllib
import re   
import json
import numpy as np
import time, random
import os

# Get URLs from starting page
def get_url_list(url):
    # Read URL and create bs object
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    # Look for all td tags on the website
    td_list = soup.find_all("td")
    # Initialize list for href
    href_table = []
    # Filter relevant tags
    for td in td_list:
        try:
            if td['class'][0] == 'title': 
                temp = td.find_all("a")[0]['href']
                href_table.append(temp)
        except:
            None
    # Return URLs for each poem
    return href_table

# Read poem title from URL
def get_titles( urls ):
    titles = map(lambda x: re.sub('[/-]',' ',x[6:])[:-1],urls)
    return titles

# Read poems from a URL list
def get_poems( url_list , max_delay = None ):
    poems = []
    project_info = []
    for ind in url_list:
        if max_delay is not None:
            sleep_time = random.randint(1,max_delay)
            time.sleep(sleep_time)
        url = 'http://www.poemhunter.com/' + ind
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html,"html.parser")
        div = soup.find_all("div")
        for dv in div:
            try:
                if dv['class'][0] == 'KonaBody':
                    try:
                        temp = dv.find_all("p")[0]
                        temp = clean(temp)
                        poems.append(temp)
                        project_info.append(url)
                        #add completed url to the log of completed urls 
                        with open("./completed_urls.txt", "a") as complete_file:
                            complete_file.write(url + '\n') 
                            complete_file.close()
                    except:
                        #add rejected urls to the log of rejected urls
                        with open("./rejected_urls.txt", "a") as rejected_file:
                            rejected_file.write(url + '\n')
                            rejected_file.close()
            except:
                None
    return poems

# Convert poems to unicode and replace html tags
def clean( item, replacements = ["<p>","</p>","<br>","<br/>"] ):
    item = item.prettify()
    for rep in replacements:
        item = item.replace(unicode(rep),"")
    return item

def crawl_poems(url , file_name = "poem", start = 1, end = 10, sleep = None, log = 25 ):
    # Initialize log_counter and empty poem list
    log_counter = 0
    poems = []
    
    # Start scraping
    for i in range( start , end ):
        
        # Show trace
        print "Iteration: " + str( i ) + " of " + str( end ) 
        
        # Add page counter 
        temp_url = url + str( i )
        
        temp_url_list = get_url_list( temp_url )
        temp_titles = get_titles( temp_url_list )
        temp_poems = get_poems( temp_url_list, max_delay = sleep )
        temp_result = zip( temp_titles , temp_poems )
        
        # Update poem list
        poems.extend( temp_result )
        
        ### HERE SHOULD BE A LOG 
        
        # Update log counter and save data to HD 
        log_counter = log_counter + 1
        
        if log_counter == log:
            
            log_file = file_name + str( i ) + '.txt'
            with open(log_file, 'w') as backup:
                json.dump(poems, backup)
                
            # Reset log counter
            log_counter = 0
            # Re-initialize poems list
            poems = []
            # Print log trace
            print("I did a backup in iteration: " + str(i) )
    
    # If data left - Save to HD
    if log_counter != log:
        log_file = file_name + str( i ) + '.txt'
        with open(log_file, 'w') as backup:
            json.dump(poems, backup, indent = 3)
    
    # Print final statement    
    print "I'm done!!! Iteration: " + str(i) + " of " + str(end)     
