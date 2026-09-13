# 90. Exercise: Functions
# Create function 
# num = [10, 2, 3, 4, 8, 11]

def highest_even(li):
	evens = []
	for item in li:
		if item % 2 == 0:
			evens.append(item)
	return max(evens)

print(highest_even([10, 2, 3, 4, 8, 11]))
	
#print(highest_even([10, 2, 3, 4, 8, 11])) # print the highest even in the list

def cats_d(li):
	cats = []
	for item in li:
		if item == 'Debu':
			cats.append(item)
		return str(cats)
print(cats_d(['Debu', 'Young', 'Kan']))
