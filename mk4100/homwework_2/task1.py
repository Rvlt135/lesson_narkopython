a = list([1, 2, 3, 4])
b = list([5, 6, 7, 8])

print(a[1], b[-1])

c = a + b

print(c)

d = c[3:5]

print(d)

d1 = [9, 10]
d.extend(d1)

print(d)

a1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c1 = set(a1) & set(b1)

print(c1)

d1 = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
d2 = list(set(d1))

print(d2)
