# 93. Scope rules
# what will the folowing output

a = 1

def confusion():
	a = 5
	return a
	
#print(a) # prints 1
print(confusion()) # prints 5
print(a)
# it will return 5

# 1 - start with local scope (like a)
# 2 - if no local scope, is there a parent local scope
def parent():
	a = 10
	def confusion():
		return a
	return confusion()
	
print(parent())
print(a)

# 3 - Global 
# 4 - Built in python functions (such as sum)
def parent():
	def confusion():
		return sum
	return confusion()
	
print(parent())
print(a)
	
