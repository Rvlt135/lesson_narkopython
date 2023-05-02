s = input("Введите набор символов:")

arr = ''.join(filter(str.isalpha, s.lower()))

l = "none"
n = 0

for i in arr:
    k = arr.count(i)

    if k == n:
        l = min(l,i)

    elif k > n:
        l = i
        n = k

print(l, n)