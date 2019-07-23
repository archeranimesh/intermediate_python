# There is no tuple comprehension.
# When we need memory efficient list, we can create a generator like range()
# This code creates a generator and not a tuple comprehensions.
my_square = (num * num for num in range(11))
print(my_square)

# TypeError: 'generator' object is not subscriptable
# print(my_square[0])

# We can iterate over the square generator like this.
try:
    while True:
        print(next(my_square))
except StopIteration as SI:
    print("stop iteraton")

# Directly convert it to a tuple
my_square = (*(num * num for num in range(11)),)
print("my_square: ", my_square)
for x in my_square:
    print(x)

# Pass the generator to tuple(), list() etc to form the corresponding collections.
my_tuple = tuple(my_square)
print("my_tuple:", my_tuple)

