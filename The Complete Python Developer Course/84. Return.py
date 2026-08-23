# 84. Return

#def sum(num1, num2):
#	return num1 + num2 # must add return to print expression
# a function should do something really well(should do one thing)
# should return something
#total = sum(10, 5)
#print(sum(10, total))

# must return at the end
def sum(num1, num2):
	def another_func(n1, n2):
		return n1 + n2 # defines but does not run it
	return another_func(num1, num2)
	
total = sum(10, 20)
print(total)

# the return keyword exits the function


