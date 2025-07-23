# 25deathsaves.py by Sanah Keswani-Santiago

import random

success = 0
failure = 0
revive = 0
is_revived = False
stable = 0
dead = 0
total = 0

for i in range(1, 101):				# Calculate probabilities of stable, dies and revives
	is_revived = False
	while True:
		roll = random.randint(1, 20)
		if roll >= 10 and roll != 20:
			success += 1
		if roll < 10 and roll != 1:
			failure += 1
		if roll == 1:
			failure += 2
		if roll == 20:
			revive += 1
			is_revived = True
		
	
		if success >= 3 and is_revived == False:
			stable += 1
			break
		if failure >= 3:
			dead += 1
			break
		if is_revived == True:
			break
	
	total += 1

prob_stable = stable / total
prob_dead = dead / total
prob_revive = revive / total

# Display table
print('Probability')
print()
print('Stable\t', 'Dies\t', 'Revives')
print(prob_stable, '\t', prob_dead, '\t', prob_revive)
