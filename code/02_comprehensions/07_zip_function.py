# Consider this dictionary.
square_dict = {num: num * num for num in range(11)}

# .items() gives a list of tuple, so if we have a list of tuple
# We should be able to convert it to a dict.
print(square_dict.items())

# list of player and scores
players = ["XXX", "YYY", "ZZZ"]
scores = [100, 98, 45]

# Players and Scores list can be combined with the help of zip.
score_card = zip(players, scores)
print(score_card)

# Use for loop to get the values.
# It returns a tuple of values.
for item in score_card:
    print(item)

# Use tuple unpacking
# the above score_card has exhauted it values.
for name, score in zip(players, scores):
    print(name, score)

# list comprehension.
score_list = [f"Name {name} had score {score}" for name, score in zip(players, scores)]
print(score_list)

# Zip with non symmetical lists
my_list1 = [1, 2, 3]
my_list2 = ["a", "b"]

# Zip will only apply to the 2 list values.
for item in zip(my_list1, my_list2):
    print(item)

# List of tuple(zip) to Dict.
score_dict = dict(zip(players, scores))
print(score_dict)

