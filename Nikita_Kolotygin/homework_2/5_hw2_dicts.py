a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4,'e': 5}

c = {}
for i in set(a.keys()|b.keys()):
    if i in a and i in b:
        c[i] = [a[i], b[i]]
    elif i in a:
        c[i] = [a[i], None]
    else:
        c[i] = [None, b[i]]

print(c)

