# 94. Global Keyword

#a = 10
#def confusion(b): # parameter b (local variable)
#	print(b)
#	a = 90
	
#confusion(300)

#total = 0

#def count():
#	global total
#	total += 1
#	return total
	
#count()
#count()
#print(count())

# += adds the value to the variable on the left
# better way to do the above
total = 1

def count(total):
	total += 1
	return total
	
print(count(total))
print(count(count(total)))
print(count(count(count(total))))

