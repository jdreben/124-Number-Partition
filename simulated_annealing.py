#!/usr/bin/env python
# boilerplate usage / reading in file
## Usage: ./simulated_annealing.py path_to_input_file max_iterations
## returns simulated annealing for input_file with smallest residue after max_iterations
import sys # to read in inputfile
if len(sys.argv) != 3:
	print "Usage: ./simulated_annealing.py path_to_input_file max_iterations"
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
	return sigma

def T(iter):
	return (10 ** 10) * (0.8 ** floor(iter / 300.0))

from math import exp, floor, e
from random import choice, random, randint
from decimal import Decimal, getcontext; getcontext().prec = 100

S = [choice([-1, 1]) for _ in range(0,len(our_list))]
S_residue = residue(S, our_list)

S_double_prime = S
S_double_prime_residue = S_residue

for iter in range(1, max_iterations):
	S_prime = S[:]; index = None
	# Choose two random indices i and j from [1,n] with i != j
	if random() < .5: # 50 / 50 chance of 1 or 2 switched
		# 2 switched
		index = randint(0,len(our_list)-1)
		S_prime[index] = -1 * S_prime[index]
	# 1 switched
	random_move = index 
	while True:
		index = randint(0, len(our_list)-1)
		if random_move != index:
			S_prime[index] = -1 * S_prime[index]
			break # makes sure the same one isn't changed twice
	# check if better than the best
	S_prime_residue = residue(S_prime, our_list)
	if S_prime_residue < S_residue:
		S = S_prime
		S_residue = S_prime_residue
	# here lies the difference from hill climbing
	else:
		print "exp looks like"
		print "residue(S_prime, our_list) " + str(residue(S_prime, our_list))
		print "residue(S, our_list) " + str(residue(S, our_list))
		print "T(float(iter)) " + str(T(float(iter)))
		pigs_fly = Decimal(e) ** Decimal(-1 * residue(S_prime, our_list) - residue(S, our_list) / T(float(iter)))
		print pigs_fly
		if random() < pigs_fly:
			if residue(S, our_list) < residue(S_double_prime, our_list):
				S_double_prime = S
				S_double_prime_residue = residue(S, our_list)

# returns the best sequence
print S_double_prime