import random
a = ['milk', 'fire', 'intent', 'gaslight']
b = ['jaba', 'toad', 'rest', 'fuckup']
print(a[1])
b[-1]='juppelle'
print(b)
c = a + b
print(c)
k = 3
d = (random.SystemRandom().sample(c, k))
print(d)
c.extend(['lyarva', 'kurva'])
print(c)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set(a).intersection(b)
print(c)
e = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
print(set(e))








