# 55genefinder.py by Sanah Keswani-Santiago

import sys
import argparse
import mcb185
import sequence

parser = argparse.ArgumentParser(description='Reports putative coding genes')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--min_orf', type=int, default=300, help='minimum open reading frame (ORF) length [%(default)i]')
arg = parser.parse_args()
print('Finding putative coding genes in', arg.file)

filename = arg.file
min_orf_length = arg.min_orf

for defline, seq in mcb185.read_fasta(filename):
	defwords = defline.split()
	name = defwords[0]
	seq = seq[0:10]
	print(seq)
	print(min_orf_length)
	
	frame_1 = seq[0:len(seq)]
	frame_2 = seq[1:len(seq)]
	frame_3 = seq[2:len(seq)]
	
	rev_seq = sequence.revcomp(seq)
	
	rev_frame_1 = rev_seq[0:len(rev_seq)]
	rev_frame_2 = rev_seq[1:len(rev_seq)]
	rev_frame_3 = rev_seq[2:len(rev_seq)]
	
	forward_frames = [frame_1, frame_2, frame_3]
	reverse_frames = [rev_frame_1, rev_frame_2, rev_frame_3]
	forward_orf_starts = []
	forward_orf_ends = []
	reverse_orf_starts = []
	reverse_orf_ends = []
	
	for frame in forward_frames:
		start = 0
		end = 3
		is_orf = False
		while True:
			codon = frame[start:end]
			if is_orf == False and codon == 'ATG':
				is_orf = True
				forward_orf_starts.append(start)
			if is_orf == True and (codon == 'TAA' or codon == 'TAG' or codon == 'TAG'):
				forward_orf_ends.append(end)
				is_orf == False
			
			start += 3
			end += 3
			#print(start, end)
			if end > len(frame): break
	
	
	for frame in reverse_frames:
		start = 0
		end = 0
		is_orf = False
		while True:
			codon = frame[start:end]
			if is_orf == False and codon == 'ATG':
				is_orf = True
				reverse_orf_starts.append(start)
			if is_orf == True and (codon == 'TAA' or codon == 'TAG' or codon == 'TAG'):
				reverse_orf_ends.append(end)
				is_orf == False
			
			start += 3
			end += 3
			if end > len(frame): break
			
	
	for forward_start, forward_end in zip(forward_orf_starts):
		length = forward_end - forward_start - 1
		print(length)
		if length >= min_orf_length:
			print(forward_start, forward_end)
			
	for reverse_start, reverse_end in zip(reverse_orf_starts):
		length = reverse_end - reverse_start - 1
		if length >= min_orf_length:
			print(reverse_start, reverse_end)
		
