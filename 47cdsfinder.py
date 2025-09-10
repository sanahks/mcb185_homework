# 47cdsfinder.py by Sanah Keswani-Santiago

import sys
import mcb185
import sequence

filename = sys.argv[1]
min_protein_length = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(filename):
	defwords = defline.split()
	name = defwords[0]
	
	frame_1 = seq[0:len(seq)]
	frame_2 = seq[1:len(seq)]
	frame_3 = seq[2:len(seq)]
	
	rev_seq = sequence.revcomp(seq)
	
	rev_frame_1 = rev_seq[0:len(rev_seq)]
	rev_frame_2 = rev_seq[1:len(rev_seq)]
	rev_frame_3 = rev_seq[2:len(rev_seq)]
	
	
	trans_frame_1 = sequence.translate_full(frame_1)
	trans_frame_2 = sequence.translate_full(frame_2)
	trans_frame_3 = sequence.translate_full(frame_3)
	trans_frame_4 = sequence.translate_full(rev_frame_1)
	trans_frame_5 = sequence.translate_full(rev_frame_2)
	trans_frame_6 = sequence.translate_full(rev_frame_3)
	
	seg_1 = trans_frame_1.split('*')
	seg_2 = trans_frame_2.split('*')
	seg_3 = trans_frame_3.split('*')
	seg_4 = trans_frame_4.split('*')
	seg_5 = trans_frame_5.split('*')
	seg_6 = trans_frame_6.split('*')
	
	segments = seg_1 + seg_2 + seg_3 + seg_4 + seg_5 + seg_6
	
	prot_list = []
	proteins = []
	
	for segment in segments:
		for i in range(len(segment)):
			if segment[i] == 'M':
				prot_list.append(segment[i:len(segment)])
				
	
	for pr in prot_list:
		if len(pr) >= min_protein_length:
			proteins.append(pr)
			

	for i in range(0, 3):
		print('>' + name + '-prot-' + str(i))
		print(proteins[i] + '*')
		
	
