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

# better way to do the above
total = 0

def count(total):
	total += 1
	return total
	
count(total)
count(total)
print(count(count(count(total))))
