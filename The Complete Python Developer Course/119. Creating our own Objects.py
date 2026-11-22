# 119. Creating our own Object
# Example
class PlayerCharacter:# Singular
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'
# Below is instantiation of the method.
player1 = PlayerCharacter('Darby', 44)
player2 = PlayerCharacter('Tom', 21)
player1.attack = 50

print(player1.name, player1.age)
print(player2.name, player2.age)
print(player1.run())
print(player2.age)
print(player1)
print(player2)
print(player1.attack)