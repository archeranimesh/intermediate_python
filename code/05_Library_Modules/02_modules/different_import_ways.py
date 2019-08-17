# We can import in these 3 ways.
# This below import is valid, but should be avoided
# The below import clutters existing namespace.

#from my_math_function import *
#print(add_number(1,2))

# The below approach is more cleaner.
from my_math_function import add_number
print(add_number(1,2))


