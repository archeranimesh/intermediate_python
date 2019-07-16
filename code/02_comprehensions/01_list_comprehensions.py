# Change the name in a list to upper case.
names = ["xxx", "yyy", "zzz"]
upper_case_list = []
for name in names:
    upper_case_list.append(name.upper())

print(upper_case_list)

# We can reduce the step by using list comprehensions.
# The above example is of map, where each element of input
# list is present in the output list.
upper_list = [name.upper() for name in names]
print(upper_list)

# Convert in to list of tuple.
len_list_tuple = [(name, len(name)) for name in names]
print(len_list_tuple)

# Use with f string.
f_string_list = [f"the name is {name}" for name in names]
print(f_string_list)
