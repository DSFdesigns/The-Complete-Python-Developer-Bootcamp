# Dictionary Methods 2
user = {
	'basket': [1,2,3],
	'greet': 'hello',
	'age': 20
}

#print('hello' in user.keys()) 
#print(user.items()) # is a Tuple
#print(user.clear()) # prints empty dictionary

#user2 = user.copy()
#print(user2.clear())
#print(user2)

#print(user.pop('age')) # Removes and returns the value
#print(user.popitem()) # Removes last item or some pair
print(user.update({'ages': 55})) # Updates age to 55
print(user)

cats = {
	'shrine': ['chubby', 'young'],
	'river': 'black and white',
	'stream': ['house', 'black']
}

print(cats.update({'road': 'black'}))
print(cats)
