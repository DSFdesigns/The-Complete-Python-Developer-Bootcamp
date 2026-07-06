# 41. Password Checker (my solution)
user_name = input('What is your Username: ') # Username
password = input('What is your Password: ') # Password
password_length = len(password)
masked = '*' * len(password)

print(f'{user_name} your password is {masked}, and is {password_length} characters long.')
# Password as *****
# print('*' * 10)

# Instructor solution
#username = input('What is your username? ')
#password = input('What is your password? ')
#password_length = len(password)
#hidden_password = '*' = password_length

#pirnt(f'{username}, your password, {hidden_password}, is {password_length} letters long.')
