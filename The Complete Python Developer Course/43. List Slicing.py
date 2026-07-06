# 43. List Slicing (lists are mutable and can be changed)
# list slicing creates a new list
amazon_cart = [
'notebooks', 
'sunglasses',
'toys',
'grapes'
]
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:] # original list stays the same
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)


