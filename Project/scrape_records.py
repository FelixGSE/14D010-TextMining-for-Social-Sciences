
def to_record_search_string(string):
	search_string = re.sub('\s','+',string)
	return search_string

def crawl_awards(song_list):

	reject_string = "Unfortunately that search produced no certifications"
	main = "http://www.riaa.com/gold-platinum/?tab_active=default-award&se="
	global_list = []
	error_list = []
	for idx,sub_list in enumerate(song_list):
		
		try:

			trace_start(idx)

			delay = random.randint(1,5)
			time.sleep(delay)


			temp_artist = sub_list[0]
			temp_song = sub_list[1]
			temp_lyrics = sub_list[2]
			


			temp_url_artist = to_record_search_string(str(temp_artist))
			temp_url_song = to_record_search_string(str(temp_song))
			search_url = main + temp_url_artist + '+' + temp_url_song 

			html = urllib.urlopen(search_url)
			soup = BeautifulSoup(html)

			if reject_string in str(soup):
				new_song = []
				new_song.append( 0 )
				new_song.append( temp_artist )
				new_song.append( temp_song )
				new_song.append( temp_lyrics )
					
				global_list.append(new_song)
				trace_finish(idx)
				continue

			record_string = soup.find_all('p',  class_="share_text")
			
			reference_string = str(temp_song).upper()
			if reference_string[-1].isspace():
				reference_string = reference_string[:-1]

			p_counter = 0
			g_counter = 0

			for idx,record in enumerate(record_string):
				bool1 = reference_string in str(record)[0:100]
				bool2 = "Gold" in str(record)[0:100]
				bool3 = "Platinum" in str(record)[0:100]
				if bool1 == True and bool2 == True:
					g_counter = g_counter + 1
				if bool1 == True and bool3 == True:
					p_counter = p_counter + 1

			new_song = []


			if p_counter is not 0:
				new_song.append( 2 )
				new_song.append( temp_artist )
				new_song.append( temp_song )
				new_song.append( temp_lyrics )
				trace_finish(idx)
				global_list.append(new_song)
				continue
			
			if g_counter is not  0:
				new_song.append( 1 )
				new_song.append( temp_artist )
				new_song.append( temp_song )
				new_song.append( temp_lyrics )
				trace_finish(idx)
				global_list.append(new_song)
				continue

			if len(new_song) == 0:
				new_song.append( 0 )
				new_song.append( temp_artist )
				new_song.append( temp_song )
				new_song.append( temp_lyrics )
				trace_finish(idx)
				global_list.append(new_song)
				continue
		except: 
			error_list.append(idx)
			print "I found an Error"
			trace_finish(idx)

	return [global_list,error_list]



