# Slice is a way to get a copy of a portion of list/string/tuple.
# Slice is possible on any ordered collection where index with numbers are possible

my_list = list(range(10))
# First element
print(my_list[0])
# last element
print(my_list[-1])
# slice, start at 1 index, ends at 3-1 = 2 index
print(my_list[1:3])
# copy of orginal list
new_list = my_list[:]

# Negative Index.
# -1 starts from end, -2 after that and so on.
print(my_list[-1])
# Get first element
print(my_list[-len(my_list)])

# Steps.
# Slice takes a 3rd argument which is steps.
print(my_list[::2])
# reverse a list
print(my_list[::-1])
