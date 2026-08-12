# 80. Find Duplicates in the list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

# print the duplicate values in a list

for values in some_list:
	if some_list.count(values) > 1:
		if values not in duplicates:
			duplicates.append(values)
print("Duplicate Values are: ", duplicates)