def read(name):
	with open(name) as data_file:
		data = json.load(data_file)
	return data

def save(name,file):
	with open(name, 'w') as songs:
	    json.dump( file, songs, indent = 3 )
	print "Dumped File"


def trace_start(number):
		print '*****************************'
		print 'Started Iteration: ' + str(number) 
		print '-----------------------------'

def trace_finish(number):
		print 'Finished Iteration: ' + str(number) 
		print '*****************************'
		print '\n . \n .\n .'
