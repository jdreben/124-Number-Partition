#!/usr/bin/env python
# boilerplate usage / reading in file
## Usage: ./repeated_random.py path_to_input_file max_iterations
## returns random sequence for input_file with smallest residue after max_iterations
import sys # to read in inputfile
import heapq

if len(sys.argv) != 3:
	print "Usage: ./repeated_random.py path_to_input_file max_iterations"
	sys.exit(0)
input_file = sys.argv[1]
max_iterations = int(sys.argv[2])
# most memory conservative way to read it in 
# but shouldn't be an issue because 100 or less
list = []
with open(input_file) as FileObj:
    for line in FileObj:
       list.append(-int(line)) # cast to int
# end boilerplate, begin KK

heapq.heapify(list)
print list

for i in range(len(list)):
	if len(list) == 1:
		break
	else:
		x = heapq.heappop(list)
		y = heapq.heappop(list)
		heapq.heappush(list, x - y)
		print list

print -(heapq.heappop(list))
