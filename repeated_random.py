#!/usr/bin/env python
# boilerplate usage / reading in file
## Usage: ./repeated_random.py path_to_input_file max_iterations
## returns random sequence for input_file with smallest residue after max_iterations

from kk import run as runKK
import sys
from random import randint

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

def prepartition(list_size):
	
	partition = []
	for i in range(list_size):
		partition.append(randint(0, list_size-1))
	return partition

def runPP(our_list, max_iterations):
	list_size = len(our_list)
	residue = sys.maxint

	for n in range(max_iterations):
		P = prepartition(list_size)
		# print "partition is " + str(P)
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
		# 			list[P[p] - 1] = list[p] + list[q]
		# 			# del list[p]
		# 			# del list[q-1]
		# 			list[q] = 0
		# 		q += 1
		# 	p += 1

		# final method
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
		# 			print len(list)
		# print "list getting KK'd is " + str(list)
		new_residue = runKK(list)
		residue = min(residue, new_residue)

	return residue

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
	print "Repeated Random Result " + str(run(our_list, max_iterations))





