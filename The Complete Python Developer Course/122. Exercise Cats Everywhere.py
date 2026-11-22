# Exercise Cats Everywhere
# Given the below class:
# 1 Instantiate the Cat object with 3 cats.
# 2 Create a function that finds the oldest cat.
# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2

class Cat:
    species = 'mammal'

    def _init_(self, name, age):
        self.name = name
        self.age = age

gato1 = Cat('Debu', 18)
gato2 = Cat('Young', 10)
gato3 = Cat('Kan', 20)

print(gato1.shout())