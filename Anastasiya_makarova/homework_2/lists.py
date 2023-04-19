#task 1
first_list = ['murino', 'is', 'the', 'best', 'city', 'on' 'earth']
second_list = ['I', 'love', 'Neapolitan', 'pizza']
#task 2
print(first_list[1])
#task 3
second_list[-1]='polpette'
print(second_list)
#task4
joined_list = first_list+second_list
print(joined_list)
#task 5
slice_list = joined_list[0:1] + joined_list[6:8]
print(slice_list)
#task 6
joined_list.extend(['pupa', 'lupa'])
print(joined_list)
#task 7
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list(set(a) & set(b)))
#task 8
a = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
print(list(set(a)))



