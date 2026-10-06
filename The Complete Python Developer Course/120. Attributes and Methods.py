# 120. Attributes and Methods

# Example
"""
class PlayerCharacter:# Singular
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Darby', 44)
player2 = PlayerCharacter('Tom', 21)

# print(player1.run())
# print(player2.age)
# print(player1)
# print(player2)
# help(player1)
"""
# Example 2
class PlayerCharacter:# Singular
    # Class object attribute
    membership = True # All objects won't change
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
         self.name = name #attributes dynamic
         self.age = age

    def shout(self):
        print(f'my name is {self.name}')

player1 = PlayerCharacter('Darby', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1.shout())
print(player2.shout())
