# 64. Truthy vs Falsey
is_old = bool('hello')
is_licenced = bool(5)

password = '123'
username = 'johnny'

#print(bool('hello')) # Are true
#print(bool(None)) # Is false

if password and username:# Is True print if False dont print
    print('You are old enough to drive, and you have a licence!.')
else:
    print('You cannot drive yet!')
