# 42ntcomp.py by Sanah Keswani-Santiago

import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):	# GC Composition
	defwords = defline.split()
	name = defwords[0]
	gc = 0
	for nt in seq:
		if nt == 'C' or nt == 'G': gc += 1
	print(name, gc/len(seq))
	
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):	# Individual Variables
	defwords = defline.split()
	name = defwords[0]
	A = 0
	C = 0
	G = 0
	T = 0
	N = 0
	for nt in seq:
		if	nt == 'A': A+= 1
		elif nt == 'C': C += 1
		elif nt == 'G': G += 1
		elif nt == 'T': T += 1
		else:			N += 1
	print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):	# List Variation
	defwords = defline.split()
	name = defwords[0]
	counts = [0, 0, 0, 0, 0]
	for nt in seq:
		if nt == 'A': counts[0] += 1
		elif nt == 'C': counts[1] += 1
		elif nt == 'G': counts[2] += 1
		elif nt == 'T': counts[3] += 1
		else:			counts[4] += 1
	print(name, end=' ')
	for n in counts: print(n/len(seq), end=' ')
	print()
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):	# Indexing with str.find()
	defwords = defline.split()
	name = defwords[0]
	nts = 'ACGTN'
	counts = [0] * len(nts)
	for nt in seq:
		idx = nts.find(nt)
		counts[idx] += 1
	print(name, end=' ')
	for n in counts: print(n/len(seq), end=' ')
	print()
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):	# Counting Any Letter
	defwords = defline.split()
	name = defwords[0]
	nts = []
	counts = []
	for nt in seq:
		if nt not in nts:
			nts.append(nt)
			counts.append(0)
		idx = nts.index(nt)
		counts[idx] += 1
	print(name)
	for nt, n in zip(nts, counts):
		print(nt, n, n/len(seq))
	print()
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):	# Counting with str.count()
	defwords = defline.split()
	name = defwords[0]
	print(name, end=' ')
	for nt in 'ACGTN':
		print(seq.count(nt) / len(seq), end=' ')
	print()
	
	
