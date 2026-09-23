# 95. Nonlocal keyword (refers to parent local)
#def outer():
#    x = "local"
#    def inner():
#        nonlocal x
#        x = "nonlocal"
#        print("inner:", x)

#   inner()
#    print("outer:", x)

#outer()

# 1 - start with local
# 2 - Parent local?
# 3 - Global
# Used in closures

# Practice area:
def debu():
	d = "boss"
	def young():
		nonlocal d
		d = "nonlocal"
		print("young:", d)
		
	young()
	print("debu", d)
		
debu()
