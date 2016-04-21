# Second, generate 50 random instances of the problem as described above.
# For each instance, find the result from using the Karmarkar-Karp algorithm. 
# Also, for each instance, run a repeated random, a hill climbing, and a simulated annealing algorithm,
# using both representations, each for at least 25,000 iterations.

from kk import run as kk
from simulated_annealing import simAnneal as simulated_annealing
from repeated_random import run as repeated_random
from random import randint

iterations = 25000
kk_results, sa_results, rr_results  = [], [], []
for loop in range(0, 50):
	print "at loop {}".format(str(loop))
	# generate a new one each iteration
	this_loop_list = [randint(0, 10 ** 12) for _ in range(0, 100)]
	# print "loop is {}, this_loop_list is {}".format(str(loop), str(this_loop_list))
	kk_result = kk(this_loop_list[:])

	kk_results.append(kk_result)
	# print "kk_result " + str(kk_result)
	# print "sending this_loop_list " + str(this_loop_list) + " to anneal"
	sa_result = simulated_annealing(this_loop_list, iterations)
	sa_results.append(sa_result)
	# print "sa_result " + str(sa_result)
	rr_result = repeated_random(this_loop_list, iterations)
	rr_results.append(rr_result)
	# print "rr_result " + str(rr_result)

import matplotlib.pyplot as plt

plt.plot(kk_results, color='blue')
plt.plot(sa_results, color='red')
plt.plot(rr_results, color='green')
plt.show()