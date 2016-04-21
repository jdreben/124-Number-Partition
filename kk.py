#!/usr/bin/env python
# boilerplate usage / reading in file
## Usage: ./repeated_random.py path_to_input_file max_iterations
## returns random sequence for input_file with smallest residue after max_iterations
import sys # to read in inputfile
import heapq

def run(list):
	# most memory conservative way to read it in 
	# but shouldn't be an issue because 100 or less
	
	# end boilerplate, begin KK

	heapq.heapify(list)

	for i in range(len(list)):
		if len(list) == 1:
			break
		else:
			x = heapq.heappop(list)
			y = heapq.heappop(list)
			heapq.heappush(list, x - y)

	return -(heapq.heappop(list))

def newRun(list, P):
	size = len(P)
	for i in range(size):
		for j in range(size - i):
			if P(i) == P(j):
				if list(i) >= list(j):
					list(i) = list(i) + list(j)
					list(j) = 0
				else:
					list(j) = list(i) + list(j)
					list(i) = 0
	

if len(sys.argv) != 2:
	'''
	print "Usage: ./repeated_random.py path_to_input_file"
	sys.exit(0)
	'''
else:
	# run normally
	input_file = sys.argv[1]
	list = []
	with open(input_file) as FileObj:
	    for line in FileObj:
	       list.append(-int(line)) # cast to int
	print run(list)

