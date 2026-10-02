# # Paste from my Mac Mini M4 file (to below)
# # Lesson 21 Numbers
# # int is a number
# print(2 + 4)
# print(2 - 4)
# print(2 * 4)
# print(2 / 4)
#
#
# # 23. Developer Fundamentals
# print(3 + (2 * 3))
# print(type(5 * 5))
#
# print(9 / 9)

#00P
# class BigObject: # Class can be instantiated to make instances.
#     #code
#     pass
#
# obj1 = BigObject() # instanciate
# obj2 = BigObject()
# obj3 = BigObject()
# print(type(None))
# print(type(True))
# print(type(5.5))
# print(type('Hi'))
# print(type([]))
# print(type(()))
# print(type({}))
# print(type(obj1))

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