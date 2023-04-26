#1*
a_arr = [1, 5, 2, 9, 2, 9, 1]
print(*[i for i in a_arr if a_arr.count(i) == 1])