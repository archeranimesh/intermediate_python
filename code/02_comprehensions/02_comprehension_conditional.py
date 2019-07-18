# How to filter values in list comprehenisons.
squares = [num ** 2 for num in range(10)]
print(squares)

# Print only even and odd squares seperately.
# The conditional comes at the end.
even_square = [num ** 2 for num in range(10) if num % 2 == 0]
print(even_square)

odd_square = [num ** 2 for num in range(10) if num % 2 == 1]
print(odd_square)

# Comma seperated string.
print(", ".join(str(num) for num in even_square))
print(", ".join(str(num) for num in odd_square))
