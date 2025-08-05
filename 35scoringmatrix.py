# 35scoringmatrix.py by Sanah Keswani-Santiago

import sys

# Get values from the command line
alphabet = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

print('  ', end='  ')
for letter in alphabet:				# Print the first row (alphabet)
	print(letter, end='   ')
print()

for i in range(0, len(alphabet)):	# Print the first column (alphabet) and the scoring matrix
	print(alphabet[i], end='  ')
	for j in range(0, len(alphabet)):
		if alphabet[j] == alphabet[i]:
			print(match, end='  ')
		else:
			print(mismatch, end ='  ')
	print()
