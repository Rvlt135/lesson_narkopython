

#create lists
t_list1 = [1,2,3,4,5,"Mama","Rama"]
t_list2 = [3,1,"Papa","Mama"]

#2-nd element of 1 list
print(t_list1[1])

#new value for last element of 2 list
t_list2[-1] = "Banana"
print(t_list2)

#new list with sum of both lists
t_list = t_list1 + t_list2
print(t_list)

#slice of t_list
print(t_list[-1::-2])

#2 elements added
t_list = t_list + ["Dad","Crab"]
print(t_list)

#7
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list(set(a) & set(b)))

#8 unique values

c = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
d = c
print(list(set(c) & set(d)))