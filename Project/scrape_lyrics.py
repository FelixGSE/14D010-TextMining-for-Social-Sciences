# ----------------------------------------------------------------
# Convert string to required form
# ----------------------------------------------------------------

def to_search_string(string):
	search_string = re.sub('\s','-',string)
	return search_string

# ----------------------------------------------------------------
# Crawl lyrics from songlyrics
# ----------------------------------------------------------------

def crawl_lyrics(list_of_songs,trace=True):
	complete_lyrics = []
	for idx,song in enumerate(list_of_songs):
		sub_list = []
		try:
			delay = random.randint(1,5)
			time.sleep(delay)
			main = 'http://www.songlyrics.com/'
			temp_artist = to_search_string(song[1])
			temp_song = to_search_string(song[0])
			search_url = main + temp_artist + '/' + temp_song + "-lyrics/"
			html = urllib.urlopen(search_url)
			soup = BeautifulSoup(html)
			raw_text = soup.find(id='songLyricsDiv')
			clean_text = raw_text.getText()
			sub_list.append(song[1])
			sub_list.append(song[0])
			sub_list.append(clean_text)
			complete_lyrics.append(sub_list)
		except:
			sub_list.append(song[1])
			sub_list.append(song[0])
			sub_list.append('')
			complete_lyrics.append(sub_list)
		if trace == True:
			print '*****************************'
			print "Finished iteration " + str(idx) 
			print '*****************************'
			print ".\n.\n.\n"
	return complete_lyrics