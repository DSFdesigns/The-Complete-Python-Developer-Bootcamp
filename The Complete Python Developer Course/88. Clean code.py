# 88. Clean code
def is_even(num):
	if num % 2 == 0:
		return True
	elif num % 2 != 0:
		return False
		
print(is_even(51))

# Clean this code up: Example 1
def is_even(num):
	if num % 2 == 0:
		return True
	else:
		return False

print(is_even(50))

# Clean this code up: Example 2
def is_even(num):
	if num % 2 == 0:
		return True
	return False
	
print(is_even(51))

# Clean ths code up: Example 3
def is_even(num):
	return num % 2 == 0
		
print(is_even(50))

# practice
def is_equal(num):
 return num == 2
 
print(is_equal(3))
