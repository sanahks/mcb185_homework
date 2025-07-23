# 20demo.py by Sanah Keswani-Santiago

import random

t = 1, 2	# tuple
print(t)
print(type(t))

# Mixture of types in a tuple
person = 'Steve', 21, 57891.50	# name, age, yearly income
print(person)

def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y
	
print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)
print(m[0], m[1])

# While loops
"""
while True:
	print('hello')
"""
	

i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break
	

i = 0
while i < 3:
	i = i + 1
	print('hey', i)
	

i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)


# For loops (i in range)
for i in range(1, 10, 3):
	print(i)

for i in range(0, 5):
	print(i)

for i in range(5):
	print(i)
	
for i in range(0, 5, 1):
	print(i)
	
for i in range(4, -1, -1): print(i)

# For loops (item in container)
basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)
	
for i in range(len(basket)):
	print(basket[i])

# Nesting
for i in range(7):
	if i % 2 == 0: print(i, 'is even')
	else:		   print(i, 'is odd')

# Random numbers
for i in range(5):
	print(random.random())

for i in range(3):
	print(random.randint(1, 6))
	
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())
