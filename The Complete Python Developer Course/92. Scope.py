# 92. Scope - what variables do I hace access to?
if True:
	x = 10 # is a global scope
	
def some_func():
	total = 100 # not a global scope (a function is like a new world)
	
print(x)

 
