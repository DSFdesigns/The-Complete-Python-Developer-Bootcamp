# 74. enumerate

#for i, char in enumerate((1, 2, 3)): # index of each item on the enumerate
#	print(i, char)
	
for i, char in enumerate(list(range(100))):
	if char == 50:
		print(f'index of 50 is: {i}')
