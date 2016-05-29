def read(name):
	with open(name) as data_file:
		data = json.load(data_file)
	return data

