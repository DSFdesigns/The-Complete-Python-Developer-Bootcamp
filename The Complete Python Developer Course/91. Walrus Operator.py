# 91. Walrus operator := (new feature)
# Assigns values to variables as part of a larger expression.

a = 'hellooooooooooo'

# if (len(a) > 10):
# 	print(f"too long {len(a)} elements")
	
if ((n := len(a)) > 10):					# assigns n to a
	print(f"too long {n} elements")
	
while ((n := len(a)) > 1):
	print(n)
	a = a[:-1] 
	
print(a)

# practice


