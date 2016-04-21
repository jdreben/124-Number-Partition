# Second, generate 50 random instances of the problem as described above.
# For each instance, find the result from using the Karmarkar-Karp algorithm. 
# Also, for each instance, run a repeated random, a hill climbing, and a simulated annealing algorithm,
# using both representations, each for at least 25,000 iterations.

from kk import run as kk
from simulated_annealing import simAnneal as simulated_annealing
from hill_climbing import run as hill_climbing
from repeated_random import run as repeated_random
from random import randint

iterations = 25000
kk_results, sa_results, rr_results, hc_results  = [], [], [], []
for loop in range(0, 20):
	print "At loop {}".format(str(loop))
	# generate a new one each iteration
	this_loop_list = [randint(0, 10 ** 12) for _ in range(0, 100)]

	kk_result = kk(this_loop_list[:])
	kk_results.append(kk_result)
	print "kk_result " + str(kk_result)
	rr_result = repeated_random(this_loop_list, iterations)
	rr_results.append(rr_result)
	print "rr_result " + str(rr_result)
	hc_result = hill_climbing(this_loop_list, iterations)
	hc_results.append(hc_result)
	print "hc_result " + str(hc_result)
	sa_result = simulated_annealing(this_loop_list, iterations)
	sa_results.append(sa_result)
	print "sa_result " + str(sa_result)
	


import matplotlib.pyplot as plt
print "(blue) kk_results {}".format(str(kk_results)) 
print "(red) sa_results {}".format(str(sa_results)) 
print "(pink) hc_results {}".format(str(hc_results)) 
print "(green) rr_results {}".format(str(rr_results)) 


plt.plot(kk_results, color='blue')
plt.plot(sa_results, color='red')
plt.plot(rr_results, color='green')
plt.plot(hc_results, color='pink')
plt.show()