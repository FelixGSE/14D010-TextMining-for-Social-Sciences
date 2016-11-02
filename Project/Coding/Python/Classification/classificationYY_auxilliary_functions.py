# ----------------------------------------------------------------
# Wrapper for reading json files
# ----------------------------------------------------------------

def read(name):
	with open(name) as data_file:
		data = json.load(data_file)
	return data

# ----------------------------------------------------------------
# Wrapper for saving json files
# ----------------------------------------------------------------

def save(name,file):
	with open(name, 'w') as songs:
	    json.dump( file, songs, indent = 3 )
	print "Dumped File"

# ----------------------------------------------------------------
# Trace function to display started current iteration
# ----------------------------------------------------------------

def trace_start(number):
		print '*****************************'
		print 'Started Iteration: ' + str(number) 
		print '-----------------------------'

# ----------------------------------------------------------------
# Trace function to display finished current iteration
# ----------------------------------------------------------------

def trace_finish(number):
		print 'Finished Iteration: ' + str(number) 
		print '*****************************'
		print '\n . \n .\n .'

# ----------------------------------------------------------------
# Function to preprocess a document
# ----------------------------------------------------------------

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

# ----------------------------------------------------------------
# # Wrapper to subset a "Column" - Source Stackexchange
# ----------------------------------------------------------------

def column(matrix, i):
    return [row[i] for row in matrix]

# ----------------------------------------------------------------
# Sample n uniform distributed numbers based on unique labels 
# ----------------------------------------------------------------

def benchmark(vector,n):
    unique_values = list(set(vector))
    numbers = np.random.choice(unique_values, n)
    rchoice = numbers.tolist()
    return rchoice

# ----------------------------------------------------------------
# Compute a weighted sampling prediction - 
# Dist. based on input vecotr
# ----------------------------------------------------------------

def weighted_benchmark(vector,n):
    unique_values = list(set(vector))
    frequencies = [vector.count(value) for value in unique_values]
    total_counts = float(sum(frequencies))
    probabilities = [x / float(total_counts) for x in frequencies]
    numbers = np.random.choice(unique_values, n, p = probabilities)
    rchoice = numbers.tolist()
    return rchoice

# ----------------------------------------------------------------
# Wrapper to convert a dictionary to a list of list - 
# Source: Stackexchange
# ----------------------------------------------------------------

def dic2list(dictionary):
    my_list = []
    for key, value in dictionary.iteritems():
        my_list.append([key, value])
    return my_list

# ----------------------------------------------------------------
# Wrapper to tokenize 
# ----------------------------------------------------------------

def tokenize(list_of_strings):
    tokens = []
    for sub in list_of_strings:
        temp_tokens = sub.split()
        tokens.append(temp_tokens)
    return tokens

# ----------------------------------------------------------------
# Wrapper to untokenize
# ----------------------------------------------------------------

def untokenize(list_of_tokens):
    texts = []
    for sub in list_of_tokens:
        joined = " ".join(sub)
        texts.append(joined)
    return texts

# ----------------------------------------------------------------
# Adjust to format lda output
# ----------------------------------------------------------------

def convert_tuple(list_of_tuples,ntopics):
    array = []
    for sub in list_of_tuples:
        sub_array = []
        for tup in sub:
            sub_array.append(tup[1])
        array.append(sub_array)

    return array 

# ----------------------------------------------------------------
# Auxilliary functions to convert tuples from RF Feature selection
# ----------------------------------------------------------------

def subset_tuples(list_of_tuples, k ):
    itter_range = range(k)
    colnames = []
    for sub in itter_range:
        temp = list_of_tuples[sub][1]
        colnames.append(temp)
    return colnames

# ----------------------------------------------------------------
# Find indices of pattern in array
# ----------------------------------------------------------------

def none_index(array,pattern = None):
    indices = [i for i, e in enumerate(array) if e == pattern]
    return indices 

# ----------------------------------------------------------------
# Rep function from R
# ----------------------------------------------------------------

def rep(item, n ):
    new = []
    for i in range(n):
        new.append(item)
    return new   

# ----------------------------------------------------------------
# Process Tuples in lda
# ----------------------------------------------------------------

def process_tuples(list_of_tuples,n):
    final_list = []
    for sub in list_of_tuples:
        row = rep(None,n)
        for temp_tuple in sub:
            pos = temp_tuple[0]
            row[pos] = round(temp_tuple[1],5)
        row = [0 if itter is None else itter for itter in row]
        final_list.append(row)
    return final_list

# ----------------------------------------------------------------
# Wrapper for average of a list
# ----------------------------------------------------------------

def list_avg(array,radiant = 3):
    result = sum(array) / float(len(array))
    return round(result,radiant)


