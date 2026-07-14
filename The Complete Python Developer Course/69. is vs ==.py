# 69. is vs == ( is checks for exatct value )
print(True == 1) # True
print('' == 1) # False
print([] == 1) # False
print(10 == 10.0) # True
print([] == []) # True

# print(True is 1)
# print('' is 1)
# print([] is 1)
# print(10 is 10.0)
# print([] is [])

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
