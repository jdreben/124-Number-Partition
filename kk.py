#!/usr/bin/env python
# boilerplate usage / reading in file
## Usage: ./repeated_random.py path_to_input_file max_iterations
## returns random sequence for input_file with smallest residue after max_iterations
import sys # to read in inputfile
import heapq

def run(l):
	# expects minheap
	l = [-1 * i for i in l]
	# most memory conservative way to read it in 
	# but shouldn't be an issue because 100 or less
	# end boilerplate, begin KK

	heapq.heapify(l)

	for i in range(len(l)):
		if len(l) == 1:
			break
		else:
			x = heapq.heappop(l)
			y = heapq.heappop(l)
			heapq.heappush(l, x - y)

	return -(heapq.heappop(l))

if len(sys.argv) != 2:
	'''
	print "Usage: ./repeated_random.py path_to_input_file"
	sys.exit(0)
	'''
else:
	# run normally
	input_file = sys.argv[1]
	l = []
	with open(input_file) as FileObj:
	    for line in FileObj:
	       l.append(-int(line)) # cast to int
	print run(l)

