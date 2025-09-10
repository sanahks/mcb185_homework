# 51countgff.py by Sanah Keswani-Santiago

import gzip
import sys

count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		f = line.split()
		feature = f[2]
		if feature not in count: count[feature] = 0
		count[feature] += 1
for f, n in count.items(): print(f, n)

'''
Alternate (lines 9 and 10)
if feature not in count: count[feature] = 1
else:					 count[feature] += 1
'''

for k in sorted(count): print(k, count[k])	# Sort by Keys

for k, v in sorted(count.items(), key=lambda item: item[1]):	# Sort by Values (Lambda)
	print(k, v)
