# 48transmembrane.py by Sanah Keswani-Santiago

import sys
import mcb185
import sequence

filename = sys.argv[1]

pr_list = []

for defline, pr_seq in mcb185.read_fasta(filename):
	defwords = defline.split()
	name = defwords[0]
	
	if len(pr_seq) < 30:
		continue
		
	first_30 = pr_seq[0:30]
	after_30 = pr_seq[30:len(pr_seq)]

	w_1 = 8
	w_2 = 11
	
	for i in range(len(first_30) - w_1 + 1):
		added_kd_1 = 0
		average_kd_1 = 0
		peptide_check = False
		win_8 = first_30[i:i+w_1]
		if win_8.find('P') != -1:
			continue
		for aa in win_8:
			added_kd_1 += sequence.kd_hydropathy_index(aa)
			
		average_kd_1 = added_kd_1 / len(win_8)
			
		if average_kd_1 >= 2.5:
			peptide_check = True
			break
			
		
			
	if peptide_check == True:
		for i in range(len(after_30) - w_2 + 1):
			added_kd_2 = 0
			average_kd_2 = 0
			helix_check = False
			win_11 = after_30[i:i+w_2]
			if win_11.find('P') != -1:
				continue
			for aa in win_11:
				added_kd_2 += sequence.kd_hydropathy_index(aa)
				
			average_kd_2 = added_kd_2 / len(win_11)
				
			if average_kd_2 >= 2.0:
				helix_check = True
				break
				
		
	if peptide_check == True and helix_check == True:
		pr_list.append(defline)

for i in range(0, 10):
	print(pr_list[i])

