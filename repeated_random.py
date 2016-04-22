#!/usr/bin/env python
# boilerplate usage / reading in file
## Usage: ./repeated_random.py path_to_input_file max_iterations
## returns random sequence for input_file with smallest residue after max_iterations

from kk import run as runKK

def residue(S, A):
	sigma = 0
	for p, a in zip(S, A):
		sigma += p * a
	return abs(sigma)

def run(our_list, max_iterations):
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

def prepartition(our_list):
	from random import randint
	list_size = len(our_list)
	partition = []
	for i in range(list_size):
		partition.append(randint(1, list_size))
	return partition

def runPP(our_list, max_iterations):
	from random import randint
	P = prepartition(our_list)
	list_size = len(our_list)
	for n in range(max_iterations):
		i = randint(1, list_size)
		j = randint(1, list_size)
		while P[i] == j and i > len(P):
			i = randint(1, list_size)
		P[i] = j
	for p in range(list_size):
		for q in range(list_size):
			if P[p] == P[q] and p < len(our_list) and q < len(our_list):
				our_list.append(our_list[p] + our_list[q])
				del our_list[p], our_list[q]
	return runKK(our_list)

import sys # to read in inputfile
if len(sys.argv) != 3:
	"""
	print "Usage: ./repeated_random.py path_to_input_file max_iterations"
	sys.exit(0)
	"""
else:
	# most memory conservative way to read it in 
	# but shouldn't be an issue because 100 or less
	input_file = sys.argv[1]
	max_iterations = int(sys.argv[2])
	our_list = []
	with open(input_file) as FileObj:
	    for line in FileObj:
	       our_list.append(int(line)) # cast to int
	# end boilerplate, begin repeated_random

	#print run(our_list, int(sys.argv[2]))
	print runPP(our_list, max_iterations)





