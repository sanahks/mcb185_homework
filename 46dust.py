# 46dust.py by Sanah Keswani-Santiago

import sys
import mcb185
import math

filename = sys.argv[1]
window_size = int(sys.argv[2])
entropy_threshold = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(filename):
	mask = [False] * len(seq)
	counter = 0
	while True:
		if counter == 0:
			start = 0
			end = window_size
			s = seq[start:end]
			a = s.count('A')
			c = s.count('C')
			g = s.count('G')
			t = s.count('T')
			
			prob_a = a / len(s)
			prob_c = c / len(s)
			prob_g = g / len(s)
			prob_t = t / len(s)
			
			if prob_a != 0:
				contrib_a = prob_a * math.log2(prob_a)
			else:
				contrib_a = 0
			if prob_c != 0:
				contrib_c = prob_c * math.log2(prob_c)
			else:
				contrib_c = 0
			if prob_g != 0:
				contrib_g = prob_g * math.log2(prob_g)
			else:
				contrib_g = 0
			if prob_t != 0:
				contrib_t = prob_t * math.log2(prob_t)
			else:
				contrib_t = 0
	
			entropy = -1 * (contrib_a + contrib_c + contrib_g + contrib_t)
	
			if entropy < entropy_threshold: mask[start:end] = [True] * len(s)
	
			counter += 1
		else:
			first_nt = seq[start]
			if first_nt == 'A': a -= 1
			elif first_nt == 'C': c -= 1
			elif first_nt == 'G': g -= 1
			elif first_nt == 'T': t -= 1
			start += 1
			#end += 1
			#if end == len(seq): break
			last_nt = seq[end]
			s = seq[start:end]
			if last_nt == 'A': a += 1
			elif last_nt == 'C': c += 1
			elif last_nt == 'G': g += 1
			elif last_nt == 'T': t += 1
			#s = seq[start:end]
			
			prob_a = a / len(s)
			prob_c = c / len(s)
			prob_g = g / len(s)
			prob_t = t / len(s)
			#print(prob_a, a, len(s))
			if prob_a != 0:
				contrib_a = prob_a * math.log2(prob_a)
			else:
				contrib_a = 0
			if prob_c != 0:
				contrib_c = prob_c * math.log2(prob_c)
			else:
				contrib_c = 0
			if prob_g != 0:
				contrib_g = prob_g * math.log2(prob_g)
			else:
				contrib_g = 0
			if prob_t != 0:
				contrib_t = prob_t * math.log2(prob_t)
			else:
				contrib_t = 0
	
			entropy = -1 * (contrib_a + contrib_c + contrib_g + contrib_t)
	
			if entropy < entropy_threshold: mask[start:end+1] = [True] * (len(s) + 1)
			
			end += 1
			if end == len(seq): break
	
	new_seq = [''] * len(seq)
	for index in range(len(mask)):
		if mask[index] == True: new_seq[index] = 'N'
		else: new_seq[index] = seq[index]
	
	'''
	for index, nt in enumerate(seq):
		#print(index)
		if mask[index] == True: new_seq[index] = 'N'
		else: new_seq[index] = seq[index]
	'''
	
	print('>' + defline)
	
	start_output = 0
	end_output = 60
	
	new_seq_str = ''.join(new_seq)
	
	num_lines = 0
	while num_lines <= 10:
		print(new_seq_str[start_output:end_output])
		start_output += 60
		end_output += 60
		if end_output >= len(new_seq_str):
			print(new_seq_str[start_output:len(new_seq_str) - 1])
			break
		num_lines += 1
