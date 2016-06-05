####################################################################################################

####################################################################################################

def clean( string ):
	clean_string = re.sub(r'\(.+\)','',string)
	return( clean_string )

def crawl_charts( url ):
		html = urllib.urlopen(url).read()
		soup = BeautifulSoup(html)
		tag_list = soup.find_all('tr')
		charts = []
		for i in range(1,101):
			tag = tag_list[i]
			temp_tag = tag.find_all('a')
			try:
				temp_song = clean(temp_tag[0].get('title'))
			except:
				temp_song = ""
			try:
				temp_artist = clean(temp_tag[1].get('title'))
			except:
				temp_artist = ""
			charts.append([temp_song,temp_artist])
		return charts

def url_list(main,years):
	urls = [main+str(y) for y in years]
	return urls 

def wiki_crawl(start_url, start, end, trace = True ):
	year_list = range(start,end)
	full_url_list = url_list(start_url,year_list)
	all_songs = []
	error = []
	for idx,sub_url in enumerate(full_url_list):
		delay = random.randint(1,2)
		time.sleep(delay)
		try:
			temp_charts = crawl_charts(sub_url)
			all_songs = all_songs + temp_charts
		except:
			error.append(str(year_list[idx]))
		if trace == True:
			print '*****************************'
			print "Finished iteration " + str(idx) 
			print '*****************************'
			print ".\n.\n.\n"
	return [all_songs,error]

####################################################################################################

####################################################################################################