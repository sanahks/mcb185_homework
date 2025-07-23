# 24savingthrows.py by Sanah Keswani-Santiago

import random

total = 0
dc_5 = 0
dc_10 =  0
dc_15 = 0
dc_5_advan = 0
dc_5_disadvan = 0
dc_10_advan = 0
dc_10_disadvan = 0
dc_15_advan = 0
dc_15_disadvan = 0

for i in range(1, 101):				# Calculate success with DC 5, DC 10 and DC 15, including advantage and disadvantage
	roll_1 = random.randint(1, 20)
	roll_2 = random.randint(1, 20)
	if roll_1 >= 5:
		dc_5 += 1
	if roll_1 >= 5 and roll_2 >= 5:
		dc_5_disadvan += 1
	if roll_1 >= 5 or roll_2 >= 5:
		dc_5_advan += 1
	if roll_1 >= 10:
		dc_10 += 1
	if roll_1 >= 10 and roll_2 >= 10:
		dc_10_disadvan += 1
	if roll_1 >= 10 or roll_2 >= 10:
		dc_10_advan += 1
	if roll_1 >= 15:
		dc_15 += 1
	if roll_1 >= 15 and roll_2 >= 15:
		dc_15_disadvan += 1
	if roll_1 >= 15 or roll_2 >= 15:
		dc_15_advan += 1
	
	total += 1
	
prob_dc_5 = dc_5 / total
prob_dc_10 = dc_10 / total
prob_dc_15 = dc_15 / total
	
prob_dc_5_advan = dc_5_advan / total
prob_dc_10_advan = dc_10_advan / total
prob_dc_15_advan = dc_15_advan / total

prob_dc_5_disadvan = dc_5_disadvan / total
prob_dc_10_disadvan = dc_10_disadvan / total
prob_dc_15_disadvan = dc_15_disadvan / total

# Display table
print('Probability of Success')
print()

print('DC 5\t', 'w/A\t', 'w/D')
print(prob_dc_5, '\t', prob_dc_5_advan, '\t', prob_dc_5_disadvan)
print()

print('DC 10\t', 'w/A\t', 'w/D')
print(prob_dc_10, '\t', prob_dc_10_advan, '\t', prob_dc_10_disadvan)
print()

print('DC 15\t', 'w/A\t', 'w/D')
print(prob_dc_15, '\t', prob_dc_15_advan, '\t', prob_dc_15_disadvan)
