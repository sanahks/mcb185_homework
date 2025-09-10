# sequence.py by Sanah Keswani-Santiago

def transcribe(dna):						# Transcription
	return dna.replace('T', 'U')
	
def revcomp(dna):							# Reverse Complement
	rc = []
	for nt in dna[::-1]:
		if nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:			rc.append('N')
	return ''.join(rc)
	
def translate(dna):							# Translation
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		elif codon == 'TAG': aas.append('*')
		elif codon == 'TGA': aas.append('*')
		else:				aas.append('X')
	return ''.join(aas)
	
def translate_alt(dna):						# Translation (alternate way)
	codons = ('ATG', 'TAA', 'TAG', 'TGA')
	aminos = 'M***'
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon in codons:
			idx = codons.index(codon)		# Can be written as: aas.append(aminos[codons.index(codon)])
			aa = aminos[idx]
			aas.append(aa)
		else:
			aas.append('X')
	return ''.join(aas)
	
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)
	
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)

def translate_full(dna):							# Translation
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		elif codon == 'TAG': aas.append('*')
		elif codon == 'TGA': aas.append('*')
		elif codon == 'TTT' or codon == 'TTC': aas.append('F')
		elif codon == 'TTA' or codon == 'TTG' or codon == 'CTT' or codon == 'CTC' or codon == 'CTA' or codon == 'CTG': aas.append('L')
		elif codon == 'ATT' or codon == 'ATC' or codon == 'ATA': aas.append('I')
		elif codon == 'GTT' or codon == 'GTC' or codon == 'GTA' or codon == 'GTG': aas.append('V')
		elif codon == 'TCT' or codon == 'TCC' or codon == 'TCA' or codon == 'TCG' or codon == 'AGT' or codon == 'AGC': aas.append('S')
		elif codon == 'CCT' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG': aas.append('P')
		elif codon == 'ACT' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG': aas.append('T')
		elif codon == 'GCT' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG': aas.append('A')
		elif codon == 'TAT' or codon == 'TAC': aas.append('Y')
		elif codon == 'CAT' or codon == 'CAC': aas.append('H')
		elif codon == 'CAA' or codon == 'CAG': aas.append('Q')
		elif codon == 'AAT' or codon == 'AAC': aas.append('N')
		elif codon == 'AAA' or codon == 'AAG': aas.append('K')
		elif codon == 'GAT' or codon == 'GAC': aas.append('D')
		elif codon == 'GAA' or codon == 'GAG': aas.append('E')
		elif codon == 'TGT' or codon == 'TGC': aas.append('C')
		elif codon == 'TGG': aas.append('W')
		elif codon == 'CGT' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG': aas.append('R')
		elif codon == 'GGT' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG': aas.append('G')
	return ''.join(aas)


def kd_hydropathy_index(aa):
	if aa == 'I': hydropathy_index = 4.5
	elif aa == 'V': hydropathy_index = 4.2
	elif aa == 'L': hydropathy_index = 3.8
	elif aa == 'F': hydropathy_index = 2.8
	elif aa == 'C': hydropathy_index = 2.5
	elif aa == 'M': hydropathy_index = 1.9
	elif aa == 'A': hydropathy_index = 1.8
	elif aa == 'G': hydropathy_index = -0.4
	elif aa == 'T': hydropathy_index = -0.7
	elif aa == 'S': hydropathy_index = -0.8
	elif aa == 'W': hydropathy_index = -0.9
	elif aa == 'Y': hydropathy_index = -1.3
	elif aa == 'P': hydropathy_index = -1.6
	elif aa == 'H': hydropathy_index = -3.2
	elif aa == 'E': hydropathy_index = -3.5
	elif aa == 'Q': hydropathy_index = -3.5
	elif aa == 'D': hydropathy_index = -3.5
	elif aa == 'N': hydropathy_index = -3.5
	elif aa == 'K': hydropathy_index = -3.9
	elif aa == 'R': hydropathy_index = -4.5
	
	return hydropathy_index
