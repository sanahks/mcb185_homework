# 44skew.py by Sanah Keswani-Santiago

import sys
import mcb185
import sequence

filename = sys.argv[1]
window_size = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(filename):
	g = 0
	c = 0
	counter = 0
	defwords = defline.split()
	name = defwords[0]
	#for i in range(len(seq) -window_size +1):
	while True:
		if counter == 0:
			start = 0
			end = window_size
			s = seq[start:end]
			c = s.count('C')
			g = s.count('G')
			counter += 1
		else:
			first_nt = seq[start]
			if first_nt == 'G': g -= 1
			elif first_nt == 'C': c -= 1
			start += 1
			end += 1
			#print(len(seq))
			#print(end)
			if end == len(seq): break
			last_nt = seq[end]
			if last_nt == 'G': g += 1
			elif last_nt == 'C': c += 1
			s = seq[start:end]
			
		
	comp = (c + g) / len(s)
	skew = (g - c) / (g + c)
	print(name)
	print('GC Composition:', comp)
	print('GC Skew:', skew)
	print()
	
	
'''	
# inefficient
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	print(i, sequence.gc_comp(s), sequence.gc_skew(s))
'''
