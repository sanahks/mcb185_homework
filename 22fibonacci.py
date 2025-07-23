# 22fibonacci.py by Sanah Keswani-Santiago

num_1 = 0
num_2 = 1

for i in range(1, 10):			# Calculate the first 10 numbers in the Fibnacci sequence
	if i == 1:
		print(num_1)
		print(num_2)
	else:
		new_num = num_1 + num_2
		print(new_num)
		num_1 = num_2
		num_2 = new_num
