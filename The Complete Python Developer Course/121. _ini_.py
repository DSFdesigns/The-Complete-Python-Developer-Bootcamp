# 121. _init_

class PlayerCharacter:# Singular
# Class Object attribute
	membership = True
	def __init__(self, name = 'anonymous', age = 0):
		if (age > 18):
			self.name = name #attributes
			self.age = age

	def shout(self):
		print(f'my name is {self.name}')
        
player1 = PlayerCharacter('Davey', 22)
#player2 = PlayerCharacter('Tom', 21)
#player2.attack = 50

print(player1.shout())
