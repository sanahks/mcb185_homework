# 31entropy.py by Sanah Keswani-Santiago
import sys
import math

probs = []
for arg in sys.argv[1:]:		# Get values from the command line
	f = float(arg)
	if f <= 0 or f >= 1: sys.exit('error: not a probability')
	probs.append(f)

total = 0
for p in probs: total += p		# Check that the probabilities add to 1
if not math.isclose(total, 1.0):
	sys.exit('error: probs must sum to 1.0')

h = 0
for p in probs:					# Calculate the entropy
	h -= p * math.log2(p)

# Display the result
print(f'{h:.4f}')
