# We can add an alias to the import statement
from pprint import pprint as pp
my_dict = {num: num * num for num in range(30)}

# Ugly way of printing
print(my_dict)

# Use the alias to invoke the function.
pp(my_dict)