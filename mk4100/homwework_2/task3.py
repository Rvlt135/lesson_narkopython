a  = "Robin Singh"
b = "I love arrays they are my favorite"

a1 = a.split()
b1 = b.split()

print(a1)
print(b1)

c = ['Ivan', 'Ivanou']
d = "Minsk"
e = 'Belarus'

print("Привет, "+ c[0]+' '+ c[1]+"!" + "Добро пожаловать в " + d +' '+ e)

f = ["I", "love", "arrays", "they", "are", "my", "favorite"]

print(' '.join(f))

g = ["I", "love", "arrays", "they", "are", "my", "favorite", "asd", "dfgdfg", "dfgdg"]
g.insert(2, "asd")
del g[6]

print(g)

h = { 'a': 1, 'b': 2, 'c': 3}
i = { 'c': 3, 'd': 4,'e': 5}
j = {}
for key in (h | i):
    j[key] = [h.get(key), i.get(key)]

print(j)


k = [1, 5, 2, 9, 2, 9, 1]

print(min(k, key = k.count))


#l = "a-z"
#m = "Hello World!"
#n = "How do you do?"
#o = "One"
#p = "Oops!"
#q = "AAaooo!!!!"
#r = "a"*9000+"b"*1000

