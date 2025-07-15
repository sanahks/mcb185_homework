# 10demo.py by Sanah Keswani-Santiago

import math

print('hello, again') # greeting

print(1.5e-2)

print(1 + 1)
print(1 - 1)
print(2 * 2)
print(1 / 2)
print(2 ** 3)
print(5 // 2)
print(5 % 2)
print(5 * (2 + 1))

print(abs(-9))
print(pow(2, 3))
print(round(7.865953, ndigits=3))

print(math.ceil(6.3))
print(math.floor(9.9))
print(math.log(5))
print(math.log2(7))
print(math.log10(9))
print(math.sqrt(25))
print(math.pow(2, 6))
print(math.factorial(5))

print(0.1 * 1)
print(0.1 * 3)

a = 3							# side of triangle
b = 4							# side of triangle
c = math.sqrt(a**2 + b**2)		# hypotenuse
print(c)

print(type(a), type(b), type(c), sep=', ', end='\n')

def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
	
print (pythagoras(3, 4))

def circle_area(r): return math.pi * r**2
def rectangle_area(w, h): return w * h

def triangle_area(w, h): return rectangle_area(w, h) / 2

s = 'hello world'
print(s, type(s))

a = 2
b = 2
if a == b:
	print('a equals b')
	print(a, b)
	
def is_even(x):
	if x % 2 == 0: return True
	return False
	
print(is_even(2))
print(is_even(3))

c = a == b
print(c)
print(type(c))

if a < b: print('a < b')
elif a <= b: print('a <= b')
elif a == b: print('this will never print!')

a = 6
b = 5

if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

a = 0.3
b = 0.1 * 3
if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')

print(abs(a - b))
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')


s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')


#a = 1
#s = 'G'
#f a < s: print('a < s')   # Type Error

def silly(m, x, b):
	y = m * x + b
	
print(silly(2, 3, 4))
