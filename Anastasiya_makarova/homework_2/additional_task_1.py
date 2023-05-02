array = [1, 5, 2, 9, 2, 9, 1]

unique_num = 0
for num in array:
    unique_num ^= num
print(unique_num)