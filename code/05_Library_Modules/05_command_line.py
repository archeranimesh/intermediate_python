import sys

# We can use slice operation to only get the arguments without file name.
arguments = sys.argv[1:]
print(f"The arguments are : {arguments}")

name = input("What is your name human?: ")
print(f"Thou, shall be named {name}")