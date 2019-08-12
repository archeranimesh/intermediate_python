user_input = "a"
try:
    int(user_input)
    print(
        "int(user_input): ", int(user_input)
    )  # This line is not printed as there is exception.
except ValueError:
    print("Not a number")

d = {1: 1}
user_input = 2
try:
    int(user_input)
    print("int(user_input): ", int(user_input))
    d[user_input]
except (ValueError, KeyError) as e:  # Identifier for the exception
    # Catching 2 exception in one block.
    print("The error is ", e)
