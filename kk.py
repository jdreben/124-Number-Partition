#!/usr/bin/env python
# boilerplate usage / reading in file
## Usage: ./repeated_random.py path_to_input_file max_iterations
## returns random sequence for input_file with smallest residue after max_iterations
import sys # to read in inputfile
import heapq

def run(l):
	# expects minheap
	l = [-1 * i for i in l]
	heapq.heapify(l)

	for i in range(len(l)):
		if len(l) == 1:
			break
		else:
			x = heapq.heappop(l)
			y = heapq.heappop(l)
			heapq.heappush(l, x - y)

	return -(heapq.heappop(l))

def runPP(list, P):
	APrime = makeAPrime(list, P)
	heapq.heapify(APrime)

	for i in range(len(APrime)):
		if len(APrime) == 1:
			break
		else:
			x = heapq.heappop(APrime)
			y = heapq.heappop(APrime)
			heapq.heappush(APrime, x - y)

	return -(heapq.heappop(APrime))

def makeP(input):
	P = []
	list_size = input # int(sys.argv[1])
	from random import randint # max int ~ 10^18
	for i in range(list_size):
		P.append(randint(0, list_size))
	return P

def makeAPrime(list, P):
	newList = list
	size = len(P)
	for i in range(size):
		for j in range(size - i):
			if P[i] == P[j]:
				if newList[i] >= newList[j]:
					newList[i] = newList[i] + newList[j]
					newList[j] = 0
				else:
					newList[j] = newList[i] + newList[j]
					newList[i] = 0
	return newList


if len(sys.argv) != 2:
	'''
	print "Usage: ./repeated_random.py path_to_input_file"
	sys.exit(0)
	'''
else:
	# run normally
	input_file = sys.argv[1]
	list = []
	list_size = 0
	with open(input_file) as FileObj:
	    for line in FileObj:
	       list.append(-int(line)) # cast to int
	       list_size += 1
	P = makeP(list_size)
	print runPP(list, P)

