school = {"1a": 15, "7b": 20, "9d": 16, "4a": 18}
print(school["7b"])
addon = {"1a": 16, "7b": 21, "9d": 17}
school.update(addon)
addon2 = {"3a": 15, "11b": 14}
school.update(addon2)
school.pop('1a')
print(school)
print("Robin Singh".split())
print("I love arrays they are my favorite".split())
a = ['Ivan', 'Ivanou']
b = "Minsk"
c = "Belarus"
print("Привет,", (" ".join(a)), "!", "Добро пожаловать в", b, c)
d = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(' '.join(d))
w = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]
w.insert(2, 3)
del w[6]
print(w)

a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
c = {}
for key in (a | b):
    a1 = a.get(key)
    b1 = b.get(key)
    c[key] = [a1, b1]
print(c)