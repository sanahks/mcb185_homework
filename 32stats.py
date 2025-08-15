# 32stats.py by Sanah Keswani-Santiago

import sys
import math

std_dev_num = 0

nums = []
for arg in sys.argv[1:]:	# Get values from the command line
	num = float(arg)
	nums.append(num)

num_vals = len(nums)		# Calculate the number of values and the mean
mean = sum(nums) / num_vals

for i in range(len(nums)):	# Calculate the standard deviation
	diff = nums[i] - mean
	std_dev_num += diff ** 2

std_dev = std_dev_num / (num_vals - 1)

nums.sort()
min = nums[0]				# Calculate the minimum and the maximum
max = nums[len(nums) - 1]

if num_vals % 2 == 0:		# Calculate the median
	index_1 = math.floor(num_vals / 2) - 1
	index_2 = index_1 + 1
	median = (nums[index_1] + nums[index_2]) / 2
if num_vals % 2 != 0:
	index = math.floor(num_vals / 2)
	median = nums[index]
	
# Display the results
print('Number of values:', num_vals)
print('Minimum:', min)
print('Maximum:', max)
print('Mean:', mean)
print('Standard deviation:', std_dev)
print('Median:', median)
