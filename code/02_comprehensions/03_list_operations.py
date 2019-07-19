square = [num * num for num in range(10)]
print(square)

# Various operation on list.
# Sum() : returns the sum of list.
sum_num = sum(square)
print(sum_num)

# min() : returns minimum number in list.
min_num = min(square)
print(min_num)

# max() : returns the maximum number in list.
max_num = max(square)
print(max_num)

# sorted() : returns a sorted list.
# reverse=True, reverse the list
sort_list = sorted(square, reverse=True)
print(sort_list)

lottery_num = "1, 4, 56, 78, 98"
# Get the maximum lottery num
max_lottery = max([int(num) for num in lottery_num.split(", ")])
print(max_lottery)
