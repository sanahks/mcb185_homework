# 53dust.py by Sanah Keswani-Santiago

import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20, help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4, help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

filename = arg.file
window_size = arg.size
entropy_threshold = arg.entropy

def calculate_contribution(prob):
	if prob == 0:
		return 0
	else:
		return prob * math.log2(prob)

def calculate_entropy(prob_a, prob_c, prob_g, prob_t):
	contrib_a = calculate_contribution(prob_a)
	contrib_c = calculate_contribution(prob_c)
	contrib_g = calculate_contribution(prob_g)
	contrib_t = calculate_contribution(prob_t)
	
	ent = -1 * (contrib_a + contrib_c + contrib_g + contrib_t)
	return ent
	
for defline, seq in mcb185.read_fasta(filename):
	mask = [False] * len(seq)
	
	start = 0
	end = window_size
	s = seq[start:end]
	a = s.count('A')
	c = s.count('C')
	g = s.count('G')
	t = s.count('T')
	
	entropy = calculate_entropy(a / len(s), c / len(s), g / len(s), t / len(s))
			
	if entropy < entropy_threshold: mask[start:end] = [True] * len(s)
	
	
	while True:
		first_nt = seq[start]
		if first_nt == 'A': a -= 1
		elif first_nt == 'C': c -= 1
		elif first_nt == 'G': g -= 1
		elif first_nt == 'T': t -= 1
		start += 1
		last_nt = seq[end]
		s = seq[start:end]
		if last_nt == 'A': a += 1
		elif last_nt == 'C': c += 1
		elif last_nt == 'G': g += 1
		elif last_nt == 'T': t += 1
		
	
		entropy = calculate_entropy(a / len(s), c / len(s), g / len(s), t / len(s))
	
		if entropy < entropy_threshold: mask[start:end+1] = [True] * (len(s) + 1)
			
		end += 1
		if end == len(seq): break
	
	new_seq = [''] * len(seq)
	for index in range(len(mask)):
		if mask[index] == True and arg.lower == False: new_seq[index] = 'N'
		elif mask[index] == True and arg.lower == True: new_seq[index] = 'n'
		else: new_seq[index] = seq[index]
	
	
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

