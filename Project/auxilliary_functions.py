
# Wrapper for reading json files
def read(name):
	with open(name) as data_file:
		data = json.load(data_file)
	return data

# Wrapper for saving json files
def save(name,file):
	with open(name, 'w') as songs:
	    json.dump( file, songs, indent = 3 )
	print "Dumped File"

# Trace function used in this project to display current iteration
def trace_start(number):
		print '*****************************'
		print 'Started Iteration: ' + str(number) 
		print '-----------------------------'

# Trace function used in this project to display current iteration
def trace_finish(number):
		print 'Finished Iteration: ' + str(number) 
		print '*****************************'
		print '\n . \n .\n .'

# Function to preprocess a document
def preprocess(text, alphanum_chars, lower = True):
    # Clean word list
    stripped = re.sub(alphanum_chars,' ', text)
    # Create a list of words
    word_list = stripped.split()
    # Return output according to bool lower
    if lower == True:
        lower_words=[words.lower() for words in word_list]
        return lower_words
    else:
        return word_list

# Wrapper to subset a "Column" from a list of list - Source Stackexchange
def column(matrix, i):
    return [row[i] for row in matrix]

# Sample n uniform distributed numbers based on unique labels of input
def benchmark(vector,n):
    unique_values = list(set(vector))
    numbers = np.random.choice(unique_values, n)
    rchoice = numbers.tolist()
    return rchoice

# Compute a weighted sampling prediction - Dist. based on input vecotr
def weighted_benchmark(vector,n):
    unique_values = list(set(vector))
    frequencies = [vector.count(value) for value in unique_values]
    total_counts = float(sum(frequencies))
    probabilities = [x / float(total_counts) for x in frequencies]
    numbers = np.random.choice(unique_values, n, p = probabilities)
    rchoice = numbers.tolist()
    return rchoice

# Wrapper to convert a dictionary to a list of list - Source: Stackexchange
def dic2list(dictionary):
    my_list = []
    for key, value in dictionary.iteritems():
        my_list.append([key, value])
    return my_list

