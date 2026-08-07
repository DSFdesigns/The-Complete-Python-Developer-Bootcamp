# 78. Our First GUI
# loop thu the list when you
picture = [
	[0, 0, 0, 1, 0, 0, 0],
	[0, 0, 1, 1, 1, 0, 0],
	[0, 1, 1, 1, 1, 1, 0],
	[1, 1, 1, 1, 1, 1, 1],
	[0, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0]
	]

	# 1. iterate over picture.
		# if 0 -> print ''
		# if 1 -> print *
		# may have to use end(use google)

#for row in picture:
#	for pixel in row:
#		if (pixel == 1):
#			print('*', end='')
#		else:
#			print(' ', end='')
#	print('')

# Practice
image = [
	[0, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	]

for unit in image:
	for pixel in unit:
		if (pixel == 1):
			print('*', end='')
		else:
			print(' ', end='')
	print('')




