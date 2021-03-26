## Lists, dictionaries, sets and tuples
# Example list, mutable, maintains order, indexed
# Documentation: https://docs.python.org/3/library/stdtypes.html#list
my_list = [1,2,3,4,5,6,7,'hello','world']
print(my_list)

# Example dictionary, key, value pairs
# Documentation: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
my_dict = {'name':'john','course':'python'}
print(my_dict)

# Example set, note: sets don't allow duplicates
# Documentation: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
my_set = {1,6,2,'java','ruby',8,9,10,21,1000,'python',6}
print(my_set) # One 6 from the set declaration will be removed

# Example tuple, immutable
# Documentation: https://docs.python.org/3/library/stdtypes.html#tuple
my_tuple = ('hello','world','night','king','says','bye',8,3)
print(my_tuple)
