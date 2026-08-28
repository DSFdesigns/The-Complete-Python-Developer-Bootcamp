# *args and **kwargs (arguments and keyword arguments)

#def super_func(*args):
#	print(args) # args is a tuple
#	return sum(args)

#super_func(1, 2, 3, 4, 5)
#print(super_func(1, 2, 3, 4, 5)) # prints the sum

# **kwargs
def super_funct(name, *args, i='hi', **kwargs):
	total = 0
	for items in kwargs.values():
		total += items
	return 	sum(args) + total
	
print(super_funct('Andre', 1,2,3,4,5, num1 = 5, num2 = 10))

# Rule of the order: params, *args, default parameters, **kwargs
