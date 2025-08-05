# 30demo.py by Sanah Keswani-Santiago

import math
import sys

# Strings
s = 'hello world'
print(s)

# String delimiters
s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

# String operators
s = 'hello'
s = 'hello' + 'world'
polyA = 'A' * 100

'''
if s1 < s2:
if s1 > s2:
if s1 == s2:
'''

# String functions
'''
len(s)
chr(n)
ord(c)
'''

# String methods
print(s.upper())
print(s)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

# String formatting

# f strings
print(f'{math.pi}')	# does nothing special
print(f'{math.pi:.3f}')	# 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')	# exponent notation
print(f'{"hello world":>20}')	# right justify with space filler
print(f'{"hello world":.>20}')	# right justify with dot filler
print(f'{20:<10} {10}')	# left justify

# str.format()
print('{} {:.3f}'.format('str.format', math.pi))

# printf
print('%s %.3f' % ('printf', math.pi))

# Indexes
seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq:
	print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])
	

s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])

print(s[0:5], s[:5])	# both ABCDE
print(s[5:len(s)], s[5:])	# both FGHIJ

print(s, s[::], s[::1], s[::-1])

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)
	
# Tuples
tax = ('Homo', 'sapiens', 9606)	# construct tuple
print(tax)

'''
s[0] = 'C'
tax[0] = 'human'
'''

print(tax[0])
print(tax[::-1])

# Enumerate
nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
	
for i, nt in enumerate(nts):
	print(i, nt)
	
# Zip
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])
	
for nt, name in zip(nts, names):
	print(nt, name)
	
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	
# Lists
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

# list() function
items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

# Split
text = 'good day          to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

# Join
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

# Searching
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
# print('index Z?', alph.index('Z'))

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

# Command Line Data (sys.argv)
print(sys.argv)

# Converting types
i = int('42')
x = float('0.61803')
print(i * x)

# x = float('hello')

# Pairwise comparision
# Loops to make comparisons
'''
for i in range(0, len(list)):
	for j in range(X, len(list)):

X = 0: all combinations
X = i: half-matrix with diagonal
X = i+1: half-matrix without diagonal
'''
