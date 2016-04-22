# Second, generate 50 random instances of the problem as described above.
# For each instance, find the result from using the Karmarkar-Karp algorithm. 
# Also, for each instance, run a repeated random, a hill climbing, and a simulated annealing algorithm,
# using both representations, each for at least 25,000 iterations.

from kk import run as kk
from random import randint

from simulated_annealing import simAnneal as simulated_annealing
from simulated_annealing import simAnnealPP as simulated_annealingPP

from hill_climbing import run as hill_climbing
from hill_climbing import runPP as hill_climbingPP

from repeated_random import run as repeated_random
from repeated_random import runPP as repeated_randomPP

iterations = 25000
kk_results, sa_results, rr_results, hc_results  = [], [], [], []
sa_resultsPP, rr_resultsPP, hc_resultsPP  = [], [], []
for loop in range(0, 50):
	print "At loop {}".format(str(loop))
	# generate a new one each iteration
	this_loop_list = [randint(0, 10 ** 12) for _ in range(0, 100)]

	# first representation
	kk_result = kk(this_loop_list[:])
	kk_results.append(kk_result)
	print "kk_result " + str(kk_result)
	rr_result = repeated_random(this_loop_list[:], iterations)
	rr_results.append(rr_result)
	print "rr_result " + str(rr_result)
	hc_result = hill_climbing(this_loop_list[:], iterations)
	hc_results.append(hc_result)
	print "hc_result " + str(hc_result)
	sa_result = simulated_annealing(this_loop_list[:], iterations)
	sa_results.append(sa_result)
	print "sa_result " + str(sa_result)

	# second representation
	rr_resultPP = repeated_randomPP(this_loop_list[:], iterations)
	rr_resultsPP.append(rr_resultPP)
	print "rr_resultPP " + str(rr_resultPP)
	hc_resultPP = hill_climbingPP(this_loop_list[:], iterations)
	hc_resultsPP.append(hc_resultPP)
	print "hc_resultPP " + str(hc_resultPP)
	sa_resultPP = simulated_annealingPP(this_loop_list[:], iterations)
	sa_resultsPP.append(sa_resultPP)
	print "sa_resultPP " + str(sa_resultPP)
	


import matplotlib.pyplot as plt
print "(blue) kk_results {}".format(str(kk_results)) 
print "(red) sa_results {}".format(str(sa_results)) 
print "(pink) hc_results {}".format(str(hc_results)) 
print "(green) rr_results {}".format(str(rr_results)) 
print "\n"
print "(red) sa_resultsPP {}".format(str(sa_resultsPP)) 
print "(pink) hc_resultsPP {}".format(str(hc_resultsPP)) 
print "(green) rr_resultsPP {}".format(str(rr_resultsPP)) 

## four graphs
# normal and log plot of each representation

plt.plot(kk_results, color='blue', label='KK')
plt.plot(sa_results, color='red', label='SA')
plt.plot(rr_results, color='green', label='RR')
plt.plot(hc_results, color='pink', label='HC')

legend = plt.legend(loc='upper right', shadow=True, fontsize='large')
# Put a nicer background color on the legend.
# legend.get_frame().set_facecolor('#00FFCC')
plt.title("1st representation")
plt.xlabel("instance")
plt.ylabel("residue")

plt.show()

plt.semilogy(kk_results, color='blue', label='KK')
plt.semilogy(sa_results, color='red', label='SA')
plt.semilogy(rr_results, color='green', label='RR')
plt.semilogy(hc_results, color='pink', label='HC')

legend = plt.legend(loc='upper right', shadow=True, fontsize='large')
# Put a nicer background color on the legend.
# legend.get_frame().set_facecolor('#00FFCC')

plt.title("1st representation")
plt.xlabel("instance")
plt.ylabel("log residue")

plt.show()

# 2nd representation
plt.plot(kk_results, color='blue', label='KK')
plt.plot(sa_resultsRR, color='red', label='SA')
plt.plot(rr_resultsRR, color='green', label='RR')
plt.plot(hc_resultsRR, color='pink', label='HC')

legend = plt.legend(loc='upper right', shadow=True, fontsize='large')
# Put a nicer background color on the legend.
# legend.get_frame().set_facecolor('#00FFCC')
plt.title("2nd representation")
plt.xlabel("instance")
plt.ylabel("residue")

plt.show()

plt.semilogy(kk_results, color='blue', label='KK')
plt.semilogy(sa_resultsRR, color='red', label='SA')
plt.semilogy(rr_resultsRR, color='green', label='RR')
plt.semilogy(hc_resultsRR, color='pink', label='HC')

legend = plt.legend(loc='upper right', shadow=True, fontsize='large')
# Put a nicer background color on the legend.
# legend.get_frame().set_facecolor('#00FFCC')
plt.title("normal plot, 2nd representation")
plt.xlabel("instance")
plt.ylabel("log residue")

plt.show()