# Second, generate 50 random instances of the problem as described above.
# For each instance, find the result from using the Karmarkar-Karp algorithm. 
# Also, for each instance, run a repeated random, a hill climbing, and a simulated annealing algorithm,
# using both representations, each for at least 25,000 iterations.

from kk import run as kk
from simulated_annealing import simAnneal as simulated_annealing
from repeated_random import run as repeated_random

iterations = 25000
kk_results, sa_results, rr_results  = [], [], []
for loop in range(0, 50):
	# generate a new one each iteration
	input = [randint(0, 10 ** 12) for _ in range(0, 100)]
	kk_results.append(kk(input))
	sa_results.append(simulated_annealing(input, iterations))
	rr_results.append(repeated_random(input, iterations))

import matplotlib.pyplot as plt

plt.plot(kk_results, color='blue')
plt.plot(sa_results, color='red')
plt.plot(rr_results, color='green')
plt.show()