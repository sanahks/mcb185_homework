# 23triples.py by Sanah Keswani-Santiago

import math

for a in range(1, 100):				# Calculate Pythagorean triples with a and b less than 100
	for b in range(1, 100):
		c = math.sqrt(a**2 + b**2)
		if c % 1 == 0:
			print(a, b, c)
