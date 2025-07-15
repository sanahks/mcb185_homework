# 11oligo.py by Sanah Keswani-Santiago

def tm(num_a, num_c, num_g, num_t):
	total_nts = num_a + num_c + num_g + num_t   # Total number of nucleotides
	
	# Calculate oligo melting temperature depending on the length of the oligo
	if total_nts <= 13:
		temp = ((num_a + num_t) * 2) + ((num_g + num_c) * 4)
	else:
		temp = 64.9 + ((41 * (num_g + num_c - 16.4)) / (num_a + num_t + num_g + num_c))
		
	return temp


print(tm(5, 7, 3, 4))
print(tm(2, 2, 2, 2))
print(tm(3, 5, 8, 2))
