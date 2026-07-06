# Formatted Strings
name = 'Johnny'
age = 55

print('Hi ' + name + '. You are ' + str(age) + ' years old')

# new formatted string method
print(f'hi {name}. You are {age}') # an f string

print('hi {}. You are {} years old'.format('Johnny', '55'))

print('hi {}. You are {} years old'.format(name, age))

print('hi {new_name}. Your are {age} years old'.format(new_name ='Sally', age=100)) 


neko = 'Gato'
ammount = 1

print('I have {} cat named {}.'.format(ammount, neko))

fname = 'Andre'
lname = 'Faulkner'
full_name = f"{fname} {lname}"
message = f"Hello, {full_name.title()}"
print(full_name)

print(message)
