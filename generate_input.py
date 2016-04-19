#!/usr/bin/env python
## Usage: ./generate_input n, where n is the size of desired list
import sys # to read in number of elements
if len(sys.argv) != 2:
	print "Usage: ./generate_input n \n Where n is the size of desired list"
	sys.exit(0)
list_size = int(sys.argv[1])
from random import randint # max int ~ 10^18
file_name = 'input_file' + sys.argv[1]
f = open(file_name, 'w')
for _ in range(0, list_size):
	f.write(str(randint(0, 10 ** 12))+"\n")
f.close(); print "Wrote list of size {} to {}".format(list_size, file_name)
