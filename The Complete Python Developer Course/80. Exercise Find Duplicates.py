# 80. Find Duplicates in the list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

# print the duplicate values in a list

#for values in some_list:
#	if some_list.count(values) > 1:
#		if values not in duplicates:
#			duplicates.append(values)
#print("Duplicate Values are: ", duplicates)

# Instructor solution
for value in some_list:
	if some_list.count(value) > 1: # if value is more than one
		if value not in duplicates:
			duplicates.append(value)
print(duplicates)


cat_list = ['debu', 'young', 'gato', 'gato', 'kan chan']
dupes = []

for cats in cat_list:
	if cat_list.count(cats) > 1:
		if cats not in dupes:
			dupes.append(cats)
print(dupes)
