#!/usr/bin/env python
# boilerplate usage / reading in file
## Usage: ./hill_climbing.py path_to_input_file max_iterations
## returns hill climbing for input_file with smallest residue after max_iterations
import sys # to read in inputfile
if len(sys.argv) != 3:
	print "Usage: ./hill_climbing.py path_to_input_file max_iterations"
	sys.exit(0)
input_file = sys.argv[1]
max_iterations = int(sys.argv[2])
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

from random import choice, random, randint

best_sequence = [choice([-1, 1]) for _ in range(0,len(our_list))]
best_residue = residue(best_sequence, our_list)

for i in range(max_iterations, 0, -1):
	this_sequence = best_sequence[:]; index = None
	# Choose two random indices i and j from [1,n] with i != j
	if random() < .5: # 50 / 50 chance of 1 or 2 switched
		# 2 switched
		index = randint(0,len(our_list)-1)
		this_sequence[index] = -1 * this_sequence[index]
	# 1 switched
	random_move = index 
	while True:
		index = randint(0, len(our_list)-1)
		if random_move != index:
			this_sequence[index] = -1 * this_sequence[index]
			break # makes sure the same one isn't changed twice
	# check if better than the best
	this_residue = residue(this_sequence, our_list)
	if this_residue < best_residue:
		best_sequence = this_sequence
		best_residue = this_residue
# returns the best sequence
print best_sequence 
print best_residue