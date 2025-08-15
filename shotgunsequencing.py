# shotgunsequencing.py by Sanah Keswani-Santiago

import random

print('Shotgun Sequencing Simulator')

genome_length = int(input('Please enter the genome length in bp: '))
max_seq_depth = int(input('Please enter the maximum sequencing depth as an integer: '))
read_length = int(input('Please enter the read length in bp: '))
max_bin = 25

depths = list(range(1, max_seq_depth + 1))

'''
seq_depth = 1
percent_list = []
row = 1
col = 1
'''
def simulate_row(depth):
	genome_hits = [0] * genome_length
	
	num_reads = (depth * genome_length) // read_length
	
	for i in range(num_reads):
		start_position = random.randint(0, genome_length - read_length)
		for j in range(read_length):
			genome_hits[start_position + j] += 1
			
	row_counts = [0] * (max_bin + 1)
	for h in genome_hits:
		if h <= max_bin:
			row_counts[h] += 1
		else:
			row_counts[max_bin] += 1
			
	row_percent = [round(100 * count / genome_length, 6) for count in row_counts]
	return row_percent
	
percent_table = [simulate_row(d) for d in depths]

table_header = ['Depth'] + [f'{coverage}x' for coverage in range(max_bin + 1)]
print('\t'.join(table_header))
for depth, row in zip(depths, percent_table):
	formatted = [f'{value:.2f}' for value in row]
	print('\t'.join([str(depth)] + formatted))
		
'''
while seq_depth <= max_seq_depth:
	genome_hits = [0] * genome_length
	num_reads = int((seq_depth * genome_length) / read_length)
	for i in range(num_reads):
		start_position = random.randint(0, genome_length - 1)
		for j in range(read_length):
			if start_position + j > genome_length - 1:
				break
			genome_hits[start_position + j] += 1
		
		max_hits = max(genome_hits)
		
		
		for num_hits in range(0, max_hits + 1):
			num_coverage = genome_hits.count(num_hits)
			percent = num_coverage / genome_length
			percent_list.append(percent)
		
	percent_list.append('*')
	seq_depth += 1
print(percent_list)

print('     ', end='  ')
for coverage in range(31):
	print(coverage, end = '     ')
print()

index = 0
depth = 1
while depth <= max_seq_depth:
	print(depth, end='    ')
	while True:
		if percent_list[index] == '*':
			print()
			index += 1
			break
		elif percent_list[index] != '*' and index != len(percent_list) - 1:
			print(percent_list[index], end='  ')
			index += 1
		elif index == len(percent_list) - 1:
			break
	depth += 1
'''
