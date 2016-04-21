#!/usr/bin/env python
# boilerplate usage / reading in file
## Usage: ./repeated_random.py path_to_input_file max_iterations
## returns random sequence for input_file with smallest residue after max_iterations

def run(input_file, max_iterations):
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
		return abs(sigma)

	from random import choice # choosing between -1 and 1
	best_sequence = [choice([-1, 1]) for _ in range(0,len(our_list))]
	best_residue = residue(best_sequence, our_list)
	for i in range(max_iterations, 0, -1):
		random_assignment = [choice([-1, 1]) for _ in range(0,len(our_list))]
		# check if better than the best
		this_residue = residue(random_assignment, our_list)
		if this_residue < best_residue:
			best_sequence = random_assignment
			best_residue = this_residue
	# returns the best sequence
	return best_residue

import sys # to read in inputfile
if len(sys.argv) != 3:
	"""
	print "Usage: ./repeated_random.py path_to_input_file max_iterations"
	sys.exit(0)
	"""
else:
	print run(sys.argv[1], int(sys.argv[2]))





