# 12phred.py by Sanah Keswani-Santiago

# Phred quality score: Q = -10 * log10(P), P = probability that base call is wrong
# ASCII char = chr(Q + 33), 33 = ASCII offset for standard Sanger FASTQ format

import math

def char_to_prob(char):
	if not char or len(char) != 1:						# Check that the character is valid
		return None
	else:
		if ord(char) < 33 or ord(char) > 126:			# Check that the ASCII value is valid
			return None
		else:
			q = ord(char) - 33
			prob = 10 ** (q / -10)
			return prob


def prob_to_char(prob):
	if prob < 0 or prob > 1:							# Check that the probability is valid
		return None
	else:
		q = -10 * (math.log10(prob))
		
		if round(q + 33) < 33 or round(q + 33) > 126:	# Check that the ASCII value is valid
			return None
		else:
			char = chr(round(q + 33))
			return char
			

print(char_to_prob('A'))
print(prob_to_char(0.001))
print(char_to_prob(''))
print(prob_to_char(2))
