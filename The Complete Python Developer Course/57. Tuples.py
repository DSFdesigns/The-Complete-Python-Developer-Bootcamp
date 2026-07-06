# 57. Tuple (like a list but immutable, cannot modify)(used for things that should not change)
my_tuple = (1, 2, 3, 4, 5)
#my_tuple[1] = 'z'

# print(5 in my_tuple)

user = {
	(1,2): [1, 2, 3],
	'greet': 'hello',
	'age': 20
}

print(user[(1,2)])
print(4 in my_tuple)



