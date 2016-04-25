#!/usr/bin/env python
# boilerplate usage / reading in file
## Usage: ./simulated_annealing.py path_to_input_file max_iterations
## returns simulated annealing for input_file with smallest residue after max_iterations

import sys # to read in inputfile
from math import exp, floor, e
from random import choice, random, randint
# from repeated_random import prepartition as prepartition
import heapq

def prepartition(list_size):
	partition = []
	for i in range(list_size):
		partition.append(randint(0, list_size-1))
	return partition

from kk import run as runKK
# def runKK(l):
# 	# expects minheap
# 	l = [-1 * i for i in l]
# 	heapq.heapify(l)

# 	for i in range(len(l)):
# 		if len(l) == 1 or len(l) == 0:
# 			break
# 		else:
# 			x = heapq.heappop(l)
# 			y = heapq.heappop(l)
# 			heapq.heappush(l, x - y)

# 	return -(heapq.heappop(l))

def residue(S, A):
	sigma = 0
	for p, a in zip(S, A):
		sigma += p * a
	return abs(sigma)

def T(iter):
	return (10 ** 10) * (0.8 ** floor(iter / 300.0))

def simAnneal(our_list, max_iterations):
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
	return S_double_prime_residue

def getNeighbor(P):
	length = len(P)
	i = choice(range(0, length)); j = P[i]
	while P[i] == j:
		j = choice(range(0, length))
	P[i] = j
	return P

def getPartition(P, our_list):
	list = our_list[:]
	# new method
	# p = 0
	# while p < len(list):
	# 	q = p + 1
	# 	while q < len(list):
	# 		if P[p] == P[q]:
	# 			# print "p is " + str(p)
	# 			# print "q is " + str(q)
	# 			# print "P[p] " + str(P[p])
	# 			# print "P[q] " + str(P[q])
	# 			# print "this fired"
	# 			list.append(list[p] + list[q])
	# 			del list[p]
	# 			del list[q-1]
	# 		q += 1
	# 	p += 1

	# final method
	list_size = len(list)
	A = [0 for _ in range(list_size)]
	for j in range(list_size):
		A[P[j]] = A[P[j]] + list[j]
	list = A[:]

	# old method
	# for p in range(list_size):
	# 	for q in range(list_size - p):
	# 		if p < min([len(list), len(P)]) and q < min([len(list), len(P)]) and P[p] == P[q]:
	# 			list.append(list[p] + list[q])
	# 			del list[p]
	# 			del list[q]

	return list

def simAnnealPP(our_list, max_iterations):
	list_size = len(our_list)
	S = prepartition(list_size)
	residue_S = runKK(getPartition(S, our_list))
	S_double_prime = S[:]
	S_double_prime_residue = residue_S

	for n in range(max_iterations):
		S_prime = getNeighbor(S)
		residue_S_prime = runKK(getPartition(S_prime, our_list))
		
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

	return S_double_prime_residue

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
	print simAnneal(our_list, max_iterations)

