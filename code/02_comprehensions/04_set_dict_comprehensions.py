# Like list we can have set and dict comprehensions.
# Set comprehensions.

# The below set is not ordered.
square_set = {num * num for num in range(11)}
print(square_set)

# Dict Comprehension
dict_square = {num: num * num for num in range(11)}
print(dict_square)

# Use f"string to create a set and dict
f_string_square_set = {f"The square of {num} is {num * num}" for num in range(5)}
for x in f_string_square_set:
    print(x)

f_string_square_dict = {num: f"the square is {num*num}" for num in range(5)}
for k, v in f_string_square_dict.items():
    print(k, ":", v)
