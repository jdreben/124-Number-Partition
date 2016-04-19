#!/usr/bin/env python
# boilerplate usage / reading in file
## Usage: ./repeated_random.py path_to_input_file max_iterations
## returns random sequence for input_file with smallest residue after max_iterations
import sys # to read in inputfile
if len(sys.argv) != 3:
	print "Usage: ./repeated_random.py path_to_input_file max_iterations"
	sys.exit(0)
input_file = sys.argv[1]
max_iterations = int(sys.argv[2])
# most memory conservative way to read it in 
# but shouldn't be an issue because 100 or less
heap = []
with open(input_file) as FileObj:
    for line in FileObj:
       heap.append(int(line)) # cast to int
# end boilerplate, begin repeated_random

heapq.heapify(heap)
print heap
