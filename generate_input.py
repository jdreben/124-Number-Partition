#!/usr/bin/env python
## Usage: ./generate_input n, where n is the size of desired list
import sys # to read in number of elements

# accessible via import
def run(input, title, verbose=False):
	list_size = input # int(sys.argv[1])
	from random import randint # max int ~ 10^18
	file_name = 'input_file' + title
	f = open(file_name, 'w')
	for _ in range(0, list_size):
		f.write(str(randint(0, 10 ** 12))+"\n")
	f.close()
	if verbose:
		print "Wrote list of size {} to {}".format(list_size, file_name)

if len(sys.argv) != 2:
	''' 
		this was for earlier when run via commandline
		now modified for usage via import as well
		print "Usage: ./generate_input n \n Where n is the size of desired list"
	'''
else:
	# run it normally in verbose mode
	run(int(sys.argv[1]), sys.argv[1], True)


