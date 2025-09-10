# 54missingkmers.py by Sanah Keswani-Santiago

import sys
import mcb185
import argparse
import sequence
import itertools

parser = argparse.ArgumentParser(description='Calculate smallest missing k-mer.')
parser.add_argument('file', type=str, help='name of fasta file')
arg = parser.parse_args()
print('Finding the smallest missing kmers in', arg.file)


for defline, seq in mcb185.read_fasta(arg.file):
	smallest_k = 0
	kcount = {}
	missing = {}
	rev_seq = sequence.revcomp(seq)
	num_missing = 0
	k = 1
	found = False
	while found == False:
		for i in range(len(seq) -k +1):
			kmer = seq[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1
			
		for i in range(len(rev_seq) -k +1):
			kmer = rev_seq[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1

		for nts in itertools.product('ACGT', repeat=k):
			kmer = ''.join(nts)
			if kmer not in kcount:
				num_missing += 1
				smallest_k = k
				if kmer not in missing: missing[kmer] = 0
				missing[kmer] += 1
				print(kmer, 0)
				found = True
					
			
					
		k += 1

print(num_missing, 'missing k-mers at k =', smallest_k)
