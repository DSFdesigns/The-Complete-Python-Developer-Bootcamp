# 68. Exercise: Logical Operators

is_magician = True
is_expert = False

# Check if magicain AND expert: if true print "You are a master magician"
# and
# check if magicain but not expert: print "At least you are getting there"

# if you're not a magician: print "You need magic powers"

#if is_magician and is_expert:
#	print("You are a master magician!")

#elif is_magician == True and is_expert == False:
#	print("At least you are getting there!")

#else:
#	print("You need magic powers!")
	
# Instructors solution:

#if is_expert and is_magician:
#	print("You are a master magician!")
	
#elif is_magician and not is_expert:
#	print("At least you are getting there!")

#elif not is_magician:
#	print("You need magic powers!")


is_red = False
is_pen = True

if is_red and is_pen:
	print("It is a red pen.")
	
elif not is_pen:
	print("It's not even a pen!")
	
elif is_pen and not is_red:
	print("The pen is not red")
