# 45colorname.py by Sanah Keswani-Santiago

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

input_list = [R, G, B]
min_dist = 255
min_name = ''
min_identifier = ''
min_rgb = []

def dist(color, inputs):
	d = 0
	for col, inp in zip(color, inputs):
		d += abs(col - inp)
	return d

fp = open(colorfile)

for line in fp:
	name, identifier, nums = line.split('\t')
	red, green, blue = nums.split(',')
	color_list = [int(red), int(green), int(blue)]
	distance = dist(color_list, input_list)
	if distance < min_dist:
		min_dist = distance
		min_name = name
		min_identifier = identifier
		min_rgb = color_list
fp.close()

print('RGB Input:', input_list)
print()
print('Closest Color Match:')
print('Name:', min_name)
print('Hex Identifier:', min_identifier)
print('RGB:', min_rgb)
