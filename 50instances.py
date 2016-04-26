# Second, generate 50 random instances of the problem as described above.
# For each instance, find the result from using the Karmarkar-Karp algorithm. 
# Also, for each instance, run a repeated random, a hill climbing, and a simulated annealing algorithm,
# using both representations, each for at least 25,000 iterations.

from kk import run as kk
from random import randint
import pandas as pd # just to cleanly write out info

from simulated_annealing import simAnneal as simulated_annealing
from simulated_annealing import simAnnealPP as simulated_annealingPP

from hill_climbing import run as hill_climbing
from hill_climbing import runPP as hill_climbingPP

from repeated_random import run as repeated_random
from repeated_random import runPP as repeated_randomPP


# for our report, we'd like 4 tables
# one for kk, rr, hc, ra
# rows will be [1..50] iterations
# columns will be ['iteration', 'time', 'result', 'result from partioning']
# each iteration shares the input file between methods and method representations
index = pd.Series(range(50))
columns_ = ['time', 'result']
columns = ['time', 'result', 'time with partioning', 'result with partioning']
kk_df = pd.DataFrame(index=index, columns=columns_,dtype='float').fillna(0)
rr_df = pd.DataFrame(index=index, columns=columns, dtype='float').fillna(0)
hc_df = pd.DataFrame(index=index, columns=columns, dtype='float').fillna(0)
sa_df = pd.DataFrame(index=index, columns=columns, dtype='float').fillna(0)

iterations = 25000
kk_results, sa_results, rr_results, hc_results  = [], [], [], []
kk_times, sa_times, rr_times, hc_times = [], [], [], []
sa_resultsPP, rr_resultsPP, hc_resultsPP  = [], [], []
sa_timesPP, rr_timesPP, hc_timesPP = [], [], []
for loop in range(0, 50):
	print "At loop {}".format(str(loop))
	# generate a new one each iteration
	this_loop_list = [randint(0, 10 ** 12) for _ in range(0, 100)]

	# first representation
	kk_result = kk(this_loop_list[:])
	kk_results.append(kk_result[0])
        kk_times.append(kk_result[1])
        kk_df['time'][loop] = kk_result[1]
        kk_df['result'][loop] = kk_result[0]
	print "kk_result " + str(kk_result[0])

	rr_result = repeated_random(this_loop_list[:], iterations)
	rr_results.append(rr_result[0])
        rr_times.append(rr_result[1])
        rr_df['time'][loop] = rr_result[1]
        rr_df['result'][loop] = rr_result[0]
	print "rr_result " + str(rr_result[0])

	hc_result = hill_climbing(this_loop_list[:], iterations)
	hc_results.append(hc_result[0])
        hc_times.append(hc_result[1])
        hc_df['time'][loop] = hc_result[1]
        hc_df['result'][loop] = hc_result[0]
	print "hc_result " + str(hc_result[0])

	sa_result = simulated_annealing(this_loop_list[:], iterations)
	sa_results.append(sa_result[0])
        sa_times.append(sa_result[1])
        sa_df['time'][loop] = sa_result[1]
        sa_df['result'][loop] = sa_result[0]
	print "sa_result " + str(sa_result[0])

	# second representation
	rr_resultPP = repeated_randomPP(this_loop_list[:], iterations)
	rr_resultsPP.append(rr_resultPP[0])
        rr_timesPP.append(rr_resultPP[1])
        rr_df['time with partioning'][loop] = rr_resultPP[1]
        rr_df['result with partioning'][loop] = rr_resultPP[0]
	print "rr_resultPP " + str(rr_resultPP[0])

	hc_resultPP = hill_climbingPP(this_loop_list[:], iterations)
	hc_resultsPP.append(hc_resultPP[0])
        hc_timesPP.append(hc_resultPP[1])
        hc_df['time with partioning'][loop] = hc_resultPP[1]
        hc_df['result with partioning'][loop] = hc_resultPP[0]
	print "hc_resultPP " + str(hc_resultPP[0])

	sa_resultPP = simulated_annealingPP(this_loop_list[:], iterations)
	sa_resultsPP.append(sa_resultPP[0])
        sa_timesPP.append(sa_resultPP[1])
        sa_df['time with partioning'][loop] = sa_resultPP[1]
        sa_df['result with partioning'][loop] = sa_resultPP[0]
	print "sa_resultPP " + str(sa_resultPP[0])


# now write them to csv
kk_df.to_csv('kk_df.csv')
sa_df.to_csv('sa_df.csv')
rr_df.to_csv('rr_df.csv')
hc_df.to_csv('hc_df.csv')

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
plt.savefig("normal-1st-2.png")
plt.clf()
# plt.show()

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
plt.savefig('log-1st-2.png')
plt.clf()
# plt.show()

# 2nd representation
plt.plot(kk_results, color='blue', label='KK')
plt.plot(sa_resultsPP, color='red', label='SA')
plt.plot(rr_resultsPP, color='green', label='RR')
plt.plot(hc_resultsPP, color='pink', label='HC')

legend = plt.legend(loc='upper right', shadow=True, fontsize='large')
# Put a nicer background color on the legend.
# legend.get_frame().set_facecolor('#00FFCC')
plt.title("2nd representation")
plt.xlabel("instance")
plt.ylabel("residue")
plt.savefig('normal-2nd-2.png')
plt.clf()
# plt.show()

plt.semilogy(kk_results, color='blue', label='KK')
plt.semilogy(sa_resultsPP, color='red', label='SA')
plt.semilogy(rr_resultsPP, color='green', label='RR')
plt.semilogy(hc_resultsPP, color='pink', label='HC')

legend = plt.legend(loc='upper right', shadow=True, fontsize='large')
# Put a nicer background color on the legend.
# legend.get_frame().set_facecolor('#00FFCC')
plt.title("2nd representation")
plt.xlabel("instance")
plt.ylabel("log residue")

plt.savefig('log-2nd-2.png')
plt.clf()
# plt.show()
