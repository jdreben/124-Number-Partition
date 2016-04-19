#!/usr/bin/env python
# boilerplate usage / reading in file
## Usage: ./repeated_random.py path_to_input_file max_iterations
## returns random sequence for input_file with smallest residue after max_iterations
import sys # to read in inputfile
if len(sys.argv) != 3:
	print "Usage: ./repeated_random.py path_to_input_file max_iterations"
	sys.exit(0)
input_file = sys.argv[1]
max_iterations = sys.argv[2]
# most memory conservative way to read it in 
# but shouldn't be an issue because 100 or less
our_list = []
with open(input_file) as FileObj:
    for line in FileObj:
       our_list.append(int(line)) # cast to int
# end boilerplate, begin repeated_random

def residue(S, A):
	sigma = 0
	for p, a in zip(S, A):
		sigma += p * a
	return sigma

from random import choice # choosing between -1 and 1
best_sequence = [random.choice([-1, 1]) for _ in range(0,len(our_list))]
best_residue = residue(best_sequence)
for (i = max_iterations; i > 0; i--):
	random_assignment = [random.choice([-1, 1]) for _ in range(0,len(our_list))]
	this_residue = residue(random_assignment)
	if this_residue < best_residue:
		best_sequence = random_assignment
		best_residue = this_residue
# returns the best sequence
print best_sequence





