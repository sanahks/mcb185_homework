# 34birthday.py by Sanah Keswani-Santiago

import random
import sys

# Get values from the command line
trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

num_matches = 0

for i in range(trials):				# Calculate the number of birthday matches
	calendar = [0] * days
	for j in range(people):
		birthday = random.randint(0, days - 1)
		calendar[birthday] += 1
		if calendar[birthday] > 1:
			num_matches += 1
			break

prob_shared = num_matches / trials	# Calculate the probability of a birthday match

# Display the result
print('Probability of at least one shared birthday in a classroom of', people, 'people:', prob_shared)
