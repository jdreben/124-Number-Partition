#!/usr/bin/env python
# boilerplate usage / reading in file
## Usage: ./simulated_annealing.py path_to_input_file max_iterations
## returns simulated annealing for input_file with smallest residue after max_iterations

import sys, time # to read in inputfile / time algorithm
from math import exp, floor, e, log
from random import choice, random, randint
# from repeated_random import prepartition as prepartition
import heapq

def prepartition(list_size):
	partition = []
	for i in range(list_size):
		partition.append(randint(0, list_size-1))
	return partition

from kk import run as runKK

def residue(S, A):
	sigma = 0
	for p, a in zip(S, A):
		sigma += p * a
	return abs(sigma)

def T(iter):
	return log((10 ** 10) * (0.8 ** floor(iter / 300.0)))

def simAnneal(our_list, max_iterations):
        t0 = time.time()
        # print "got to simAnneal " + str(our_list)
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
			pigs_fly = exp(-1 * (residue(S_prime, our_list) - residue(S, our_list)) / T(iter))
			if random() < pigs_fly:
				S = S_prime
		if residue(S, our_list) < residue(S_double_prime, our_list):
			S_double_prime = S
			S_double_prime_residue = residue(S, our_list)

	# returns the best sequence
        t1 = time.time()
	return (S_double_prime_residue, t1 - t0)

def getNeighbor(P):
	length = len(P)
	i = choice(range(0, length)); j = P[i]
	while P[i] == j:
		j = choice(range(0, length))
	P[i] = j
	return P

def getPartition(P, our_list):
	list = our_list[:]

	# final method
	list_size = len(list)
	A = [0 for _ in range(list_size)]
	for j in range(list_size):
		A[P[j]] = A[P[j]] + list[j]
	list = A[:]

	return list

def simAnnealPP(our_list, max_iterations):
        t0 = time.time()
	list_size = len(our_list)
	S = prepartition(list_size)
	residue_S = runKK(getPartition(S, our_list))[0]
	S_double_prime = S[:]
	S_double_prime_residue = residue_S

	for n in range(max_iterations):
		S_prime = getNeighbor(S)
		residue_S_prime = runKK(getPartition(S_prime, our_list))[0]
		if residue_S > residue_S_prime:
			S = S_prime[:]
			residue_S = residue_S_prime
		else:
			pigs_fly = exp(-1 * (residue_S_prime - residue_S) / T(float(n)))
			if random() < pigs_fly:
				S = S_prime[:]
		if residue_S < S_double_prime_residue:
			S_double_prime = S[:]
			S_double_prime_residue = residue_S
        t1 = time.time()
	return (S_double_prime_residue, t1 - t0)

if len(sys.argv) != 3:
	'''
	print("Usage: ./simulated_annealing.py path_to_input_file max_iterations")
	sys.exit(0)
	'''
else:

	input_file = sys.argv[1]
	max_iterations = int(sys.argv[2])
	# most memory conservative way to read it in 
	# but shouldn't be an issue because 100 or less
	our_list = []
	with open(input_file) as FileObj:
	    for line in FileObj:
	       our_list.append(int(line)) # cast to int
	# end boilerplate, begin repeated_random
	print simAnneal(our_list, max_iterations)[0]

