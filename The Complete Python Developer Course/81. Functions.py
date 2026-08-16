# 81. Functions (def = define a function)(stays in memory)
def say_hello():
	print('Hello')
say_hello() # Runs the function

# Example 2
picture = [
	[0, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0],
	[0, 0, 1, 0, 1, 0, 0],
	]
	
def show_tree():
	for image in picture:
		for pixel in image:
			if (pixel == 1):
				print('*', end='')
			else:
				print('-', end='')
		print('')
show_tree()


