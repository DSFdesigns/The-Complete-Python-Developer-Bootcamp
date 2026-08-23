# 83. Default Parameters and Keyword Arguments

# Default parameters
def say_hello(name = 'Darth Vader', emoji = '😈'):
    print(f'hello {name} {emoji}')

# Positional arguments
say_hello('Andre', '👋')
say_hello('Darbu', '👋')
say_hello('Arnold', '👋')
say_hello() # fills with the pre defined


# keyword arguments
# say_hello(emoji = '👋', name = 'Darby') # Bad practice, follow function
# say_hello(name = 'Bobby', emoji = '😹') # This is better

def call_gato(gato1 = 'Pigpen', gato2 = 'Gato'):
	print(f'Come {gato1}, come {gato2}.')
	
call_gato('Kan Chan', 'Young')
call_gato()

