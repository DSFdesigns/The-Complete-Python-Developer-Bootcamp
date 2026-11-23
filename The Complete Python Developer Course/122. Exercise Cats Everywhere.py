# Exercise Cats Everywhere
# Given the below class:
# 1 Instantiate the Cat object with 3 cats.
# 2 Create a function that finds the oldest cat.
# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def oldest_cat(li):
        oldest = []
        for item in li:
            if item % 1 == 0:
                oldest.append(item)
        return max(oldest)


gato1 = Cat('Debu', 18)
gato2 = Cat('Young', 10)
gato3 = Cat('Kan', 20)

#print(oldest_cat([gato1.age, gato2.age, gato3.age]))
print(oldest_cat)

#print(gato1.name, gato1.age)
#print(gato2.name, gato2.age)
#print(gato3.name, gato3.age)