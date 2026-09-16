# 87. Docstrings 
# Example 1:
def test(a):
	'''
	Info: this function tests and prints param a
	'''
	print(a)
test('!!!')
help(test)
print(test.__doc__)

# Example 2:
def test2(b):
	'''
	Info: this function tests and prints param b
	'''
	print(b)
test2('This in not a test!')
help(test2)
print(test2.__doc__)


