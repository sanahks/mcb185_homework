# 33birthday.py by Sanah Keswani-Santiago

import random
import sys

# Get values from the command line
trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

num_matches = 0

for i in range(trials):				# Calculate the number of birthday matches
	birthdays = []
	for j in range(people):
		day = random.randint(0, days - 1)
		if day in birthdays:
			num_matches += 1
			break
		birthdays.append(day)
		
prob_shared = num_matches / trials	# Calculate the probability of a birthday match

# Display the result
print('Probability of at least one shared birthday in a classroom of', people, 'people:', prob_shared)
