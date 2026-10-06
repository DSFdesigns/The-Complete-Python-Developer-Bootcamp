# 119. Creating our own Object

# Example
class PlayerCharacter:# Singular
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Darby', 44)
player2 = PlayerCharacter('Tom', 21)

print(player1.run())
print(player2.age)
print(player1)
print(player2)